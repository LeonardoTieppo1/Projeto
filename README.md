# Projeto
Projeto Interdisciplinar IV finalizado



O projeto foi feito na pasta de arquivos node, arquivos DB_projeto.ipynb e create.sql

## Integrantes do grupo
- Leonardo Oliveira Tieppo
- Thiago Araujo
- Elton Leal Barboza
- Pedro Henrique Pompermayer Zotelli 

## Intuito do projeto

O intuito do projeto 

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


### Para executar a raspagem:

Somente rodar o arquivo DB_projeto.ipynb
```shell
jupyter DB_projeto.ipynb
```

### Para executar a página:

```shell
cd node
```

Depois de acessar o arquivo node ir para o terminal e executar.

```node
npm start
```