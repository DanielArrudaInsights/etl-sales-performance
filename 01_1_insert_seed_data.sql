-- 1. Inserção na Tabela de Dimensão: Vendedores
-- (Necessário inserir antes de 'Vendas' devido à FK)

insert into Vendedores (id_vendedor, nome, meta_mensal, regiao) values
	(1, 'Ana Silva', 50000.00, 'Sudeste'),
	(2, 'Bruno Costa', 45000.00, 'Sul'),
	(3, 'Carla Souza', 60000.00, 'Nordeste'),
	(4, 'Diego Oliveira', 40000.00, 'Centro-Oeste'),
	(5, 'Fernanda Lima', 55000.00, 'Sudeste');

-- 2. Inserção na tabela de Dimensão: Clientes
-- (Seguindo o padrão 'C1001' mencionado no seu DDL)
insert into Clientes (id_cliente, data_cadastro) values
	('C1001', '2026-01-10'),
	('C1002', '2026-01-15'),
	('C1003', '2026-01-20'),
	('C1004', '2026-02-05'),
	('C1005', '2026-02-12');

-- 3. Inserção na Tabela Fato: Vendas
-- (Relacionando vendedores e clientes existentes)
insert into Vendas (id_venda, id_vendedor, id_cliente, valor_venda, data_venda, modelo_automovel) values
	(101, 1, 'C1001', 12500.00, '2026-02-15', 'Sedan Luxo'),
	(102, 2, 'C1002', 8900.50, '2026-02-16', 'Hatch Compacto'),
	(103, 3, 'C1003', 45000.00, '2026-02-17', 'SUV Premium'),
	(104, 1, 'C1004', 15200.00, '2026-02-18', 'Sedan Luxo'),
	(105, 5, 'C1005', 22000.00, '2026-02-19', 'Picape Adventure');
