import pandas as pd
import psycopg2
import json

# ====================================================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# ====================================================================

# ⚠️ SUBSTITUA OS VALORES ABAIXO COM SUAS CREDENCIAIS REAIS
DB_CONFIG = {
    "host": "localhost",
    "database": "portfolio_vendas_etl",
    "user": "Daniel",
    "password": "familia4676"
}


class ETLPipeline:
    """
    Pipeline de ETL Orientado a Objetos (OOP) para integrar dados de Vendas (CSV)
    e Metas de Vendedores (JSON) ao banco de dados PostgreSQL.

    Métodos:
        _get_connection: Estabelece a conexão com o PostgreSQL.
        extract_and_transform: Carrega e limpa os dados das fontes.
        load_data: Executa a carga dos dados, respeitando a ordem de FKs.
        run: Orquestra a execução das fases do pipeline.
    """

    def __init__(self, db_config: dict):
        """
        Inicializa o pipeline com as configurações do DB.

        Parâmetros:
            db_config (dict): Dicionário contendo host, database, user e password.
        """
        self.db_config = db_config
        self.conn = None
        self.cursor = None
        # DataFrames iniciais (preenchidos em extract_and_transform)
        self.df_vendedores = pd.DataFrame()
        self.df_vendas = pd.DataFrame()
        self.df_clientes = pd.DataFrame()

    def _get_connection(self):
        """
        Tenta estabelecer a conexão com o banco de dados PostgreSQL.

        Raises:
            psycopg2.Error: Se a conexão falhar devido a credenciais ou status do DB.
        """
        try:
            self.conn = psycopg2.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            print("Status: Conexão com o PostgreSQL estabelecida com sucesso.")
        except psycopg2.Error as e:
            # Imprime o erro e re-lança a exceção para interromper a execução do pipeline
            print(
                f"ERRO CRÍTICO: Falha ao conectar ao PostgreSQL. Verifique credenciais e status do DB: {e}")
            raise

    def extract_and_transform(self):
        """
        Extrai dados de múltiplas fontes (CSV e JSON) e realiza transformações
        iniciais (renomeação de colunas e desduplicação).
        """
        print("\n[FASE 1] Iniciando Extração e Transformação dos dados...")

        # 1. Extração e Transformação de Vendedores (Fonte JSON)
        try:
            # Carrega o arquivo JSON contendo as metas
            with open('metas_vendedores.json', 'r') as f:
                data_vendedores = json.load(f)

            # Normalização (Transformação) dos vendedores para um DataFrame
            self.df_vendedores = pd.DataFrame(data_vendedores)
            # Renomeação de coluna para corresponder ao padrão do DB
            self.df_vendedores = self.df_vendedores.rename(
                columns={'region': 'regiao'})
            print(
                f"Extração JSON (Vendedores): {len(self.df_vendedores)} registros estruturados.")

        except FileNotFoundError:
            print(
                "ERRO: Arquivo 'metas_vendedores.json' não encontrado. Verifique o path.")
            raise

        # 2. Extração e Transformação de Vendas (Fonte CSV)
        try:
            # Carrega o arquivo CSV principal de vendas
            self.df_vendas = pd.read_csv('vendas_brutas.csv')

            # Criação da Dimensão Clientes (Desduplicação / Normalização)
            # Seleciona IDs únicos de clientes a partir do DataFrame de vendas para a tabela dimensão.
            self.df_clientes = self.df_vendas[[
                'id_cliente']].drop_duplicates().copy()
            print(
                f"Extração CSV (Vendas): {len(self.df_vendas)} vendas processadas e {len(self.df_clientes)} clientes únicos identificados.")

        except FileNotFoundError:
            print("ERRO: Arquivo 'vendas_brutas.csv' não encontrado. Verifique o path.")
            raise

    def load_data(self):
        """
        Limpa as tabelas existentes (TRUNCATE) e carrega os dados processados no PostgreSQL.
        A ordem de inserção das tabelas é crucial devido às Foreign Keys (FKs).
        """
        print("\n[FASE 2] Iniciando a Carga (LOAD)...")

        try:
            # 1. Limpeza de Dados (TRUNCATE)
            # O CASCADE garante que as tabelas filhas (Vendas) também sejam limpas,
            # respeitando as restrições de chave estrangeira.
            self.cursor.execute(
                "TRUNCATE TABLE Vendas RESTART IDENTITY CASCADE;")
            self.cursor.execute(
                "TRUNCATE TABLE Clientes RESTART IDENTITY CASCADE;")
            self.cursor.execute(
                "TRUNCATE TABLE Vendedores RESTART IDENTITY CASCADE;")
            print("Status: Limpeza (TRUNCATE) das tabelas concluída com sucesso.")

            # 2. Carga da Dimensão Vendedores (Sem dependências FK)
            vendedores_records = [tuple(row)
                                  for row in self.df_vendedores.values]
            vendedores_insert_query = "INSERT INTO Vendedores (id_vendedor, nome, meta_mensal, regiao) VALUES (%s, %s, %s, %s)"
            self.cursor.executemany(
                vendedores_insert_query, vendedores_records)
            print(
                f"LOAD: {len(vendedores_records)} registros inseridos na tabela Vendedores.")

            # 3. Carga da Dimensão Clientes (Sem dependências FK)
            clientes_records = [tuple(row) for row in self.df_clientes.values]
            clientes_insert_query = "INSERT INTO Clientes (id_cliente) VALUES (%s)"
            self.cursor.executemany(clientes_insert_query, clientes_records)
            print(
                f"LOAD: {len(clientes_records)} registros inseridos na tabela Clientes.")

            # 4. Carga da Tabela Fato Vendas (Depende de Vendedores e Clientes)
            vendas_records = [tuple(row) for row in self.df_vendas.values]
            # A query abaixo insere na tabela Fato, referenciando as FKs já carregadas.
            vendas_insert_query = "INSERT INTO Vendas (id_venda, id_vendedor, valor_venda, data_venda, id_cliente, modelo_automovel) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.executemany(vendas_insert_query, vendas_records)
            print(
                f"LOAD: {len(vendas_records)} registros inseridos na tabela Vendas.")

            # Confirmação final da transação para persistir os dados no DB
            self.conn.commit()
            print("Status: Transação de carga concluída e dados persistidos no DB.")

        except psycopg2.Error as e:
            # Em caso de falha, desfaz todas as inserções
            self.conn.rollback()
            print(
                f"ERRO DURANTE O LOAD: Falha na inserção de dados. Transação desfeita. {e}")
            raise
        finally:
            self.close_connection()

    def close_connection(self):
        """
        Fecha a conexão ativa com o banco de dados e limpa os objetos de cursor/conexão.
        """
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Status: Conexão com o DB fechada.")

    def run(self):
        """
        Orquestrador do Pipeline ETL.
        Chama os métodos de conexão, extração/transformação e carga em sequência.
        """
        try:
            self._get_connection()
            self.extract_and_transform()
            self.load_data()
        except Exception as e:
            # Captura exceções não tratadas (ex: falhas de conexão ou FileNotFoundError)
            print("==============================================")
            print("PIPELINE ETL ENCERRADO COM ERROS.")
            print("==============================================")
            self.close_connection()


if __name__ == "__main__":
    print("==============================================")
    print("INICIANDO PIPELINE ETL (Vendas e Metas)")

    # Instancia e executa o pipeline
    pipeline = ETLPipeline(DB_CONFIG)
    pipeline.run()

    print("==============================================")
    print("PIPELINE ETL CONCLUÍDO.")
