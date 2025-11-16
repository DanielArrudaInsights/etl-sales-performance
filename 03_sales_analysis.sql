-- 03_sales_analysis.sql

-- ANÁLISE 1: Performance de Vendas por Vendedor vs. Meta (KPI Principal)
-- Mede a eficiência de cada vendedor em relação à meta de vendas mensal (KPI de Gestão).
SELECT
    v.nome AS nome_vendedor,
    v.regiao,
    v.meta_mensal,
    -- Soma o valor total de vendas do vendedor
    COALESCE(SUM(s.valor_venda), 0) AS total_vendido,
    -- Calcula o percentual de alcance da meta
    ROUND(
        (COALESCE(SUM(s.valor_venda), 0) * 100) / v.meta_mensal,
        2
    ) AS percentual_alcance
FROM
    Vendedores v
LEFT JOIN
    Vendas s ON v.id_vendedor = s.id_vendedor
GROUP BY
    v.nome, v.regiao, v.meta_mensal
ORDER BY
    percentual_alcance DESC;

-- ANÁLISE 2: Valor Médio de Venda por Modelo de Automóvel
-- Ajuda a gestão a focar em modelos de maior receita média.
SELECT
    modelo_automovel,
    COUNT(id_venda) AS total_vendas,
    -- Calcula o valor médio de venda do modelo, arredondado para inteiro
    ROUND(AVG(valor_venda)) AS valor_medio_venda_arredondado
FROM
    Vendas
GROUP BY
    modelo_automovel
ORDER BY
    valor_medio_venda_arredondado DESC;

-- ANÁLISE 3: Contagem de Vendas por Região
-- Distribuição de transações para validar o foco regional.
SELECT
    v.regiao,
    COUNT(s.id_venda) AS total_transacoes,
    COUNT(DISTINCT s.id_cliente) AS total_clientes_novos
FROM
    Vendedores v
LEFT JOIN
    Vendas s ON v.id_vendedor = s.id_vendedor
GROUP BY
    v.regiao
ORDER BY
    total_transacoes DESC;
    