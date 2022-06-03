const http = require("http")

//crirar um servidor utilizando o node tem uma requisição sendo feita
// alguem que está requisitando e tem uma resposta que esta sendo retornada para quem fez essa requisição
//basicamente são dois parametros co o req sendo tudo que está recebendo da requisição e o res vai ser tudo que quero retornar para quem fez a requisição
//.listen vai direcionar uma porta esctuada para quando chamar essa porta no host ela vai ser definir, quero que caia no servidor de criação
//.end para quem fez uma requisição
http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'application/json' });

}).listen(4001, () => console.log("Servidor rodando na porta 4001!"));