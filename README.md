# Pipeline ETL de Performance e Metas de Vendas

## Objetivo do Projeto

O propósito deste projeto é **estabelecer um Pipeline ETL (Extract, Transform, Load)** com estrutura modular.

O desenvolvimento visa:

1.  **Integrar Múltiplas Fontes:** Unificar dados de **múltiplas fontes (CSV e JSON)** em um banco de dados relacional (PostgreSQL).
2.  **Estruturar a Base:** Aplicar conceitos de **Modelagem e Estruturação de Bases de Dados** (DDL, Chaves Estrangeiras).
3.  **Gerar Insights:** Processar os dados carregados para viabilizar a criação de **KPIs de Desempenho de Vendas** estratégicos.

Este trabalho busca demonstrar a **aplicação prática de Automação de Processos** e raciocínio lógico em Python/SQL.

## Stack Tecnológica e Arquitetura

O projeto utiliza uma arquitetura modular baseada em Python, priorizando a manutenibilidade e a rastreabilidade do código.

| Componente | Tecnologia | Função no Projeto |
| :--- | :--- | :--- |
| **Arquitetura (Código)** | Python (Classes, OOP, Estrutura Modular) | Orquestração do pipeline, garantindo manutenibilidade. |
| **Transformação** | Python (Pandas) | Leitura de CSV e JSON, cruzamento de dados de vendas e metas (Data Wrangling). |
| **Modelagem e Carga** | PostgreSQL (psycopg2) | Definição de esquema relacional e inserção dos dados. |
| **Análise de Dados** | SQL | Geração de KPIs de Performance de Vendas para suporte à decisão. |

## Principais Resultados (KPIs Gerados)

Os dados foram estruturados para permitir análises de desempenho imediatas.

### 1. KPI Principal: Desempenho de Vendedores vs. Meta

Mede a eficiência de cada vendedor em relação à meta de vendas mensais.
| nome_vendedor | regiao | meta_mensal | total_vendido | percentual_alcance |
| :--- | :--- | :--- | :--- | :--- |
| Sofia Lopes | Sul | 250000.00 | 270000.00 | 108.00 |
| Ana Silva | Sudeste | 500000.00 | 480000.00 | 96.00 |
| Bruno Costa | Norte | 300000.00 | 260000.00 | 86.67 |
| Carlos Mendes | Sudeste | 450000.00 | 220000.00 | 48.89 |
| David Rocha | Nordeste | 350000.00 | 105000.00 | 30.00 |
Insight de Negócio: Sofia Lopes superou a meta (108%). O baixo desempenho de Carlos Mendes e David Rocha requer atenção imediata da gestão para investigação de causas (ex: treinamento, leads de má qualidade, ou falta de foco regional).

### 2. Valor Médio de Venda por Modelo de Automóvel

Ajuda a gestão a focar em modelos de maior ticket médio.
| modelo_automovel | total_vendas | valor_medio_venda_arredondado |
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
