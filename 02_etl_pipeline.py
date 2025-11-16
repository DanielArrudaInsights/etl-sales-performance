import pandas as pd
import psycopg2
import json

# SUBSTITUA OS VALORES ABAIXO COM SUAS CREDENCIAIS REAIS
DB_CONFIG = {
    "host": "localhost",
    "database": "portfolio_vendas_etl", 
    "user": "Daniel",          
    "password": "familia4676"         
}

class ETLPipeline:
    """
    Pipeline de ETL Orientado a Objetos (OOP) para integrar dados de Vendas (CSV)
    e Metas de Vendedores (JSON) ao PostgreSQL, utilizando prints para feedback.
    """
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = None
        self.cursor = None

    def _get_connection(self):
        """Tenta estabelecer a conexão com o banco de dados."""
        try:
            self.conn = psycopg2.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            print("Status: Conexão com o PostgreSQL estabelecida com sucesso.")
        except psycopg2.Error as e:
            print(f"ERRO CRÍTICO: Falha ao conectar ao PostgreSQL. Verifique credenciais e status do DB: {e}")
            raise

    def extract_and_transform(self):
        """Extrai dados de múltiplas fontes (CSV e JSON) e os transforma."""
        print("\n[FASE 1] Iniciando Extração e Transformação dos dados...")
        
        # 1. Extração e Transformação de Vendedores (Fonte JSON)
        try:
            with open('metas_vendedores.json', 'r') as f:
                data_vendedores = json.load(f)
            
            # Normalização (Transformação) dos vendedores para um DataFrame
            self.df_vendedores = pd.DataFrame(data_vendedores)
            self.df_vendedores = self.df_vendedores.rename(columns={'region': 'regiao'})
            print(f"Extração JSON (Vendedores): {len(self.df_vendedores)} registros estruturados.")

        except FileNotFoundError:
            print("ERRO: Arquivo 'metas_vendedores.json' não encontrado.")
            raise

        # 2. Extração e Transformação de Vendas (Fonte CSV)
        try:
            self.df_vendas = pd.read_csv('vendas_brutas.csv')
            
            # Geração de IDs únicos para a Tabela Clientes a partir dos dados de Vendas
            self.df_clientes = self.df_vendas[['id_cliente']].drop_duplicates().copy()
            print(f"Extração CSV (Vendas): {len(self.df_vendas)} vendas processadas.")

        except FileNotFoundError:
            print("ERRO: Arquivo 'vendas_brutas.csv' não encontrado.")
            raise

    def load_data(self):
        """Limpa as tabelas e carrega os dados processados na ordem correta."""
        print("\n[FASE 2] Iniciando a Carga (LOAD)...")
        
        try:
            # Limpeza com TRUNCATE (Garantia de Não-Duplicação)
            self.cursor.execute("TRUNCATE TABLE Vendas RESTART IDENTITY CASCADE;")
            self.cursor.execute("TRUNCATE TABLE Clientes RESTART IDENTITY CASCADE;")
            self.cursor.execute("TRUNCATE TABLE Vendedores RESTART IDENTITY CASCADE;")
            print("Status: Limpeza (TRUNCATE) das tabelas concluída com sucesso.")

            # Carga da Dimensão Vendedores
            vendedores_records = [tuple(row) for row in self.df_vendedores.values]
            vendedores_insert_query = "INSERT INTO Vendedores (id_vendedor, nome, meta_mensal, regiao) VALUES (%s, %s, %s, %s)"
            self.cursor.executemany(vendedores_insert_query, vendedores_records)
            print(f"LOAD: {len(vendedores_records)} registros inseridos na tabela Vendedores.")
            
            # Carga da Dimensão Clientes
            clientes_records = [tuple(row) for row in self.df_clientes.values]
            clientes_insert_query = "INSERT INTO Clientes (id_cliente) VALUES (%s)"
            self.cursor.executemany(clientes_insert_query, clientes_records)
            print(f"LOAD: {len(clientes_records)} registros inseridos na tabela Clientes.")

            # Carga da Tabela Fato Vendas
            vendas_records = [tuple(row) for row in self.df_vendas.values]
            vendas_insert_query = "INSERT INTO Vendas (id_venda, id_vendedor, valor_venda, data_venda, id_cliente, modelo_automovel) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.executemany(vendas_insert_query, vendas_records)
            print(f"LOAD: {len(vendas_records)} registros inseridos na tabela Vendas.")

            self.conn.commit()
            print("Status: Transação de carga concluída e dados persistidos no DB.")

        except psycopg2.Error as e:
            self.conn.rollback() 
            print(f"ERRO DURANTE O LOAD: Falha na inserção de dados. Transação desfeita. {e}")
            raise
        finally:
            self.close_connection()

    def close_connection(self):
        """Fecha a conexão com o banco de dados de forma segura."""
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Status: Conexão com o DB fechada.")

    def run(self):
        """Orquestrador do Pipeline ETL."""
        try:
            self._get_connection()
            self.extract_and_transform()
            self.load_data()
        except Exception as e:
            print("\n==============================================")
            print("PIPELINE ETL ENCERRADO COM ERROS.")
            print("==============================================")
            self.close_connection()

if __name__ == "__main__":
    print("==============================================")
    print("INICIANDO PIPELINE ETL (Vendas e Metas)")
    
    pipeline = ETLPipeline(DB_CONFIG)
    pipeline.run()
    
    print("==============================================")
    print("PIPELINE ETL CONCLUÍDO.")
