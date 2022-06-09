# Projeto
Projeto Interdisciplinar IV finalizado


O projeto foi feito na pasta de arquivos node, arquivos DB_projeto.ipynb e create.sql


## Integrantes do grupo
- Elton Leal Barbosa  

- Leonardo Oliveira Tieppo

- Pedro Henrique Pompermayer Zotelli 

- Thiago Caetano de Araujo

## Intuito do projeto


Como estamos a procura de estágio, a nossa motivação foi obter métricas relacionadas às vagas do mercado de tecnologia, utilizando uma visualização mais análitica das vagas.

## Execução do código

### 1. Para a executar o Banco de dados

Executar os seguintes scripts SQL:

#### A. criação da tabela:
```sql
CREATE TABLE `empregos` (
  `idVag` int(11) NOT NULL AUTO_INCREMENT,
  `vaga` varchar(255) DEFAULT NULL,
  `empresa` varchar(255) DEFAULT NULL,
  `localiza` varchar(255) DEFAULT NULL,
  `salario` varchar(255) DEFAULT NULL,
  `dataPostagem` varchar(255) DEFAULT NULL,
  `dataRaspagem` varchar(255) DEFAULT NULL,
  `requisitos` varchar(255) DEFAULT NULL,
  `job_url` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`idVag`)
);

```


#### B. criação da view:
```sql
CREATE VIEW `jobs` AS
    select
        `empregos`.`idVag` AS `idvag`,
        `empregos`.`vaga` AS `vaga`,
        `empregos`.`empresa` AS `empresa`,
        `empregos`.`localiza` AS `localiza`,
        cast((case 
            when (length(`empregos`.`salario`) = 0) then NULL 
            else replace(substr(`empregos`.`salario`,(locate(' ',`empregos`.`salario`) + 1),((locate(' ',`empregos`.`salario`,(locate(' ',`empregos`.`salario`) + 1)) - locate(' ',`empregos`.`salario`)) - 1)),'.','') end) as decimal(10,0)) AS `salario`,
        `empregos`.`dataPostagem` AS `dataPostagem`,
        `empregos`.`dataRaspagem` AS `dataRaspagem`,
        `empregos`.`requisitos` AS `requisitos`,
        `empregos`.`job_url` AS `job_url`
    from `empregos`;
```


### 2.Para executar a raspagem:

Somente rodar o arquivo DB_projeto.ipynb
```shell
jupyter DB_projeto.ipynb
```

### 3.Para executar a página:

Executar o comando no terminal para ir no arquivo node.

```shell
cd node
```

Depois de acessar o arquivo node ir para o terminal e executar.

```node
npm start
```