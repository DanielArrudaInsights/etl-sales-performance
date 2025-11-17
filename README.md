# Projeto de Portfólio: Análise de Vendas Automotivas (Power BI & DAX)

Este projeto demonstra a criação de um Dashboard de Business Intelligence para monitorar a performance de vendas de veículos. O objetivo foi transformar dados brutos em **insights acionáveis**, comprovando proficiência na modelagem de dados e na criação de medidas analíticas robustas.

---

## Demonstração Interativa e Código (Obrigatório)

O valor analítico deste projeto reside na interatividade e nos cálculos DAX customizados.

### Acesso Interativo (Recomendado para Avaliação)
Clique no link abaixo para interagir com o Dashboard completo no Power BI Service. Todos os filtros, tooltips e interatividade estão ativos.

**[Dashboard Interativo - Vendas Automotivas](https://app.powerbi.com/links/BBoXspi7PU?ctid=da49a844-e2e3-40af-86a6-c3819d704f49&pbi_source=linkShare)**

### Código-Fonte
O arquivo **.pbix** está disponível neste repositório para validação da modelagem de dados e das fórmulas DAX customizadas.

---

## Visão Geral do Dashboard
![Captura de tela do Dashboard de Vendas Finalizado - KPI 1, 2 e 3](Screenshot_Final.jpg)

## Ferramentas Utilizadas

* **Power BI:** Modelagem, Transformação (Power Query) e Visualização.
* **DAX (Data Analysis Expressions):** Criação de medidas customizadas de alta precisão.

---

## KPIs e Lógica Analítica

O dashboard foi estruturado em torno de três indicadores críticos, com foco na prova do conhecimento em DAX e agregação de dados:

### 1. KPI 1: Performance de Vendedores vs. Meta
**Lógica:** O cálculo da performance envolveu a criação de uma medida que compara Vendas Totais versus uma meta predefinida, essencial para avaliar o desempenho da equipe de forma objetiva.
**Insight:** Permite identificar rapidamente os *top-performers* e direcionar o foco da gestão para o desenvolvimento dos vendedores abaixo da linha de meta.

### 2. KPI 2: Ticket Médio de Venda por Modelo (Cálculo DAX)
**Lógica:** O valor não é uma simples média do visual, mas sim uma **Medida DAX (AVERAGE)** calculada para garantir precisão do Ticket Médio (receita média por transação) em qualquer contexto de filtro.
**Insight:** Demonstra que o modelo **"Esportivo Premium"** possui o maior valor por venda. Ação: Focar estratégias de marketing nos produtos de maior valor agregado.

### 3. KPI 3: Distribuição Regional de Vendas
**Lógica:** Utiliza a função **Contagem (Count)** dos IDs de Venda e formatação avançada para exibir o **Percentual do Total**, provando a capacidade de configurar visuais para clareza analítica.
**Insight:** Ajuda a alocar orçamentos de mídia e recursos de equipe com base nas regiões de maior volume transacional.

---

## Validação do Projeto (Próximos Passos)
* **Validar a Interatividade:** Clique no link do Power BI Service acima para uma experiência completa.
* **Validar
