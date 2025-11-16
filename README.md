# Pipeline ETL de Performance e Metas de Vendas

## Objetivo do Projeto

Este projeto demonstra a construção de um **Pipeline ETL (Extract, Transform, Load)** modular e robusto, integrando dados de **múltiplas fontes (CSV e JSON)** a um banco de dados relacional (PostgreSQL) para gerar KPIs de Performance de Vendas.

O projeto atende diretamente aos requisitos de **Automação de Processos** e **Estruturação de Bases Complexas** exigidos em vagas de Estágio em Análise de Dados com foco em BI/IA.

## Stack Tecnológica e Arquitetura

O projeto utiliza uma arquitetura modular baseada em Python, priorizando a manutenibilidade e a rastreabilidade do código.

| Componente | Tecnologia | Função no Projeto |
| :--- | :--- | :--- |
| **Arquitetura (Código)** | Python (Classes, OOP, Estrutura Modular) | Orquestração do pipeline, garantindo manutenibilidade. |
| **Transformação** | Python (Pandas) | Leitura de CSV e JSON, cruzamento de dados de vendas e metas (Data Wrangling). |
| **Modelagem e Carga** | PostgreSQL (psycopg2) | Definição de esquema relacional (Tabela Fato/Dimensão com Chaves Estrangeiras) e inserção dos dados. |
| **Análise de Dados** | SQL | Geração de KPIs de Performance de Vendas para suporte à decisão. |

## Principais Resultados (KPIs Gerados)

Os dados foram estruturados para permitir análises de desempenho imediatas.

### 1. KPI Principal: Performance de Vendedores vs. Meta

Mede a eficiência de cada vendedor em relação à meta de vendas mensal.

| nome\_vendedor | regiao | meta\_mensal | total\_vendido | **percentual\_alcance** |
| :--- | :--- | :--- | :--- | :--- |
| Sofia Lopes | Sul | 250000.00 | 270000.00 | **108.00** |
| Ana Silva | Sudeste | 500000.00 | 480000.00 | 96.00 |
| Bruno Costa | Norte | 300000.00 | 260000.00 | 86.67 |
| Carlos Mendes | Sudeste | 450000.00 | 220000.00 | 48.89 |
| David Rocha | Nordeste | 350000.00 | 105000.00 | 30.00 |

**Insight de Negócio:** Sofia Lopes superou a meta (108%). O baixo desempenho de Carlos Mendes e David Rocha requerem atenção imediata da gestão para investigar causas (ex: treinamento, leads de má qualidade, ou falta de foco regional).

### 2. Valor Médio de Venda por Modelo de Automóvel

Ajuda a gestão a focar em modelos de maior *ticket* médio.

*(Estes resultados foram extraídos do seu PostgreSQL)*

| modelo\_automovel | total\_vendas | valor\_medio\_venda\_arredondado |
| :--- | :--- | :--- |
| Esportivo Premium | 3 | 175000 |
| SUV Urbano | 4 | 133750 |
| Sedan Luxo | 3 | 126667 |

---

## Estrutura e Execução do Projeto

O pipeline ETL é orquestrado pela **Classe `ETLPipeline`** no `02_etl_pipeline.py`.

1.  **Configuração do DB:** Rodar o `01_create_sales_db.sql` no PostgreSQL.
2.  **Execução do ETL (Python):** O script limpa as tabelas, extrai o CSV e JSON e carrega os dados.
    ```bash
    python 02_etl_pipeline.py
    ```
3.  **Análise (SQL):** Geração dos KPIs.
    ```sql
    -- Rodar as queries do 03_sales_analysis.sql no cliente SQL
    ```

**Arquivos no Repositório:**

* `01_create_sales_db.sql` (Criação do Esquema DDL)
* `02_etl_pipeline.py` (Pipeline Python Modular - OOP, CSV/JSON)
* `03_sales_analysis.sql` (KPIs SQL)
* `vendas_brutas.csv` (Fonte de dados de vendas)
* `metas_vendedores.json` (Fonte de dados de metas)
