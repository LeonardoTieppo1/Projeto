/*const express = require("express");
//criação de id
const { randomUUID } = require("crypto");

//criação do app express
const app = express();

//ele não trabalha somente com json
//precisa informar qual o tipo de dado que vai ser retornado
//mirror=meio do caminho sendo tratado o incio e o fim
app.use(express.json());
//teste sem banco de dados, usando o array
const prod = [];

//inserir dado
/*
 Body=> sempre que passar os dados para minha aplicação
 Params=> parametro de rota
 Query=>fazem parte da rota mas não são necessários 


app.post("/produtos", (req, res) => {
    //nome e preço
    //para testar o post necessario baixar o rest client, colocar a url para testar a requisição
    //criar variaveis para realizar o método post no arquivo http
    const { name, price } = req.body;

    //criar um objeto do produto
    const produto = {
        id: randomUUID(),
        name,
        price
    };
    prod.push(produto);

    return res.json(produto);
});

//buscar um ou mais dados
app.get("/produtos", (req, res) => {
    return res.json(prod);
});

app.get("/produtos/:id", (req, res) => {
    const { id } = req.params;
    const produto = prod.find(produto => produto.id === id);
    return res.json(produto);

});

//put-alterar dado

app.put("/produtos/:id", (req, res) => {
    const { id } = req.params;
    const { name, price } = req.body;

    const produtoIndex = prod.findIndex(produto => produto.id === id);

    prod[produtoIndex] = {
        ...prod[produtoIndex],
        name,
        price
    };

    return res.json({ message: "Produto alterado com sucesso!" });
});

//delete-remover
app.delete("/produtos/:id", (req, res) => {
    const { id } = req.params;
    //pegar o index para remover o produto do array
    const produtoIndex = prod.findIndex(produto => produto.id === id);
    prod.splice(produtoIndex, 1);
    return res.json({
        message: "Produto removido com sucesso!"
    });

});

app.listen(4002, () => console.log("Servidor rodando na porta 4002"));
*/