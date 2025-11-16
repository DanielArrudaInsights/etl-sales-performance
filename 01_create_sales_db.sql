-- 01_create_sales_db.sql
-- Script de Definição de Dados (DDL) para o Portfólio 2.0 (Vendas e Metas)

-- Comando de limpeza: Usado no desenvolvimento para garantir que as tabelas
-- sejam recriadas do zero a cada execução (DROP TABLE IF EXISTS... CASCADE).
DROP TABLE IF EXISTS Vendas CASCADE;
DROP TABLE IF EXISTS Vendedores CASCADE;
DROP TABLE IF EXISTS Clientes CASCADE;

-- 1. Tabela de Dimensão: Vendedores
-- Contém metadados e a meta.
CREATE TABLE Vendedores (
    id_vendedor INTEGER PRIMARY KEY, -- Chave Primária: Identifica unicamente o vendedor
    nome VARCHAR(100) NOT NULL,
    meta_mensal NUMERIC(10, 2) NOT NULL, -- NUMERIC para precisão monetária de metas
    regiao VARCHAR(50)
);

-- 2. Tabela de Dimensão: Clientes
-- Contém a lista única de clientes.
CREATE TABLE Clientes (
    id_cliente VARCHAR(20) PRIMARY KEY, -- Chave Primária: Identifica unicamente o cliente (usamos VARCHAR devido ao padrão 'C1001')
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- 3. Tabela Fato: Vendas
-- A tabela central que registra as transações e liga as dimensões.
CREATE TABLE Vendas (
    id_venda INTEGER PRIMARY KEY, -- Chave Primária: Identifica unicamente cada venda
    id_vendedor INTEGER NOT NULL,
    id_cliente VARCHAR(20) NOT NULL,
    valor_venda NUMERIC(10, 2) NOT NULL, -- NUMERIC para precisão monetária do valor da venda
    data_venda DATE NOT NULL,
    modelo_automovel VARCHAR(100), -- VARCHAR para o nome do modelo (ex: 'Sedan Luxo')

    -- Configuração das Chaves Estrangeiras (FKs):
    -- Assegura a integridade referencial ao forçar que todo ID_VENDEDOR e ID_CLIENTE
    -- na tabela Vendas exista em suas respectivas tabelas de Dimensão.
    FOREIGN KEY (id_vendedor) REFERENCES Vendedores (id_vendedor),
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente)
);
