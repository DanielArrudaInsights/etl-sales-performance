# Projeto de Portfólio: Análise de Vendas Automotivas (Power BI & DAX)

Este dashboard foi desenvolvido para aprimorar a capacidade de monitoramento de KPIs de Vendas, Retenção e Performance, utilizando o Power BI e a linguagem de cálculo DAX. O objetivo principal é transformar dados brutos em insights acionáveis para apoiar decisões estratégicas na gestão de equipes e produtos de alto valor.

## Dashboard Final
![Captura de tela do Dashboard de Vendas Finalizado - KPI 1, 2 e 3](Screenshot_Final.jpg)

---

## Ferramentas e Metodologia

O projeto utilizou a metodologia de análise de dados para transformar dados transacionais (vendas) e dados de recursos humanos (vendedores) em métricas de performance e lucratividade.

* **Power BI:** Para modelagem de dados (relacionamento entre tabelas) e visualização.
* **DAX (Data Analysis Expressions):** Utilizado para criar medidas avançadas, garantindo cálculos precisos de performance e Ticket Médio.

---

## KPIs e Insights Chave para a Gestão

O dashboard foi estruturado em torno de três KPIs fundamentais:

### 1. KPI 1: Performance de Vendedores vs. Meta
**Visual:** Gráfico de Colunas Agrupadas e Linha.
**Insight:** O gráfico identifica claramente os vendedores que estão acima e abaixo da meta estabelecida. O cálculo do alcance de meta foi realizado via DAX.
**Ação:** Permite à gestão reconhecer imediatamente os top-performers e focar em estratégias de treinamento para aqueles abaixo da linha de meta.

### 2. KPI 2: Ticket Médio de Venda por Modelo
**Visual:** Gráfico de Colunas.
**Insight:** A análise, calculada através de uma **Medida DAX (AVERAGE)**, revelou que o modelo **"Esportivo Premium"** possui o Ticket Médio mais elevado.
**Ação:** O insight sugere focar esforços de marketing e vendas nos modelos de maior valor agregado, como o Esportivo Premium.

### 3. KPI 3: Distribuição Regional de Vendas
**Visual:** Gráfico de Rosca.
**Insight:** Este KPI demonstra a alocação de vendas por região. O gráfico está formatado para exibir apenas o **Percentual do Total**, destacando a concentração do volume de vendas na região mais forte.
**Ação:** Ajuda a alocar orçamentos de mídia e recursos de equipe com base nas regiões com maior volume transacional.

---

## Estrutura do Repositório

* `Dashboard_Vendas.pbix`: Arquivo editável do projeto Power BI.
* `Screenshot_Final.jpg`: Imagem de alta qualidade do dashboard finalizado.
