const express = require("express");
const app = express();
const mysql = require("mysql");
const bodyparser = require("body-parser");
app.use(bodyparser.json());
const ejs = require("ejs");
const port = 3000

app.set('view engine', 'ejs');
app.use(express.json());
app.use('/', express.static(__dirname + '/public'));

const pool = mysql.createPool({
    connectionLimit: 10,
    host: 'localhost',
    port: '3306',
    user: 'root',
    password: 'root',
    database: 'empregos'
});

const runSQL = (sql) => {
    return new Promise(function(res, rej) {
        pool.getConnection(function(err, connection) {
            if (err) rej(err);
            connection.query(sql, function(err, rows) {
                if (err) rej(err);
                else res(rows);
                connection.release();
            });
        });
    });
}

exports.listaVagas = (c) => {
    var sql = "SELECT * FROM jobs WHERE UPPER(vaga) LIKE (UPPER(?)) OR UPPER(requisitos) LIKE (UPPER(?))";
    var params = [];
    params.push('%' + c + '%');
    params.push('%' + c + '%');
    sql = mysql.format(sql, params);
    return runSQL(sql);
};

exports.qtdVagas = (c) => {
    var sql = "SELECT max(salario) as maximo, avg(salario) as media, count(idVag) as qtd FROM jobs WHERE UPPER(vaga) LIKE (UPPER(?)) OR UPPER(requisitos) LIKE (UPPER(?))";
    var params = [];
    params.push('%' + c + '%');
    params.push('%' + c + '%');
    sql = mysql.format(sql, params);
    return runSQL(sql);
};


app.get("/form", (req, res) => {
    res.render("pages/form")
});
app.post('/form', (req, res) => {
    this.listaVagas('').then((result) => {
        res.render('pages/teste', {
            empresas: result
        });
    });
});

app.get('/', (req, res) => {
    var l = '';
    if (req.query.busca) l = req.query.busca;
    this.listaVagas(l).then(jobs => {
        this.qtdVagas(l).then(qtd => {
            res.render('pages/index', {
                empresas: jobs,
                valores: qtd[0]
            });
        })
    });
})

app.get('/position', (req, res) => {
    var l = '';
    this.listaVagas(l).then((result) => {
        return res.json(result);
    });
})

app.get('/chart', (req, res) => {
    this.list('').then((result) => {
        res.render('pages/chart', {
            empresas: result
        });
    });
})


app.listen(port, () => console.log("Conectado com sucesso! Acesse o site: http://localhost:3000"));