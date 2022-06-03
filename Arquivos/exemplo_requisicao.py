# Vamos utilizar o pacote requests para fazer requisições HTTP:
# https://docs.python-requests.org/en/master/
#
# Para isso, ele precisa ser instalado via pip (de preferência com o VS Code fechado):

import requests

def listarPessoas():
	resultado = requests.get("https://academico.espm.br/testeapi/listar")

	# Imprime algumas informações simples da resposta
	print(resultado.status_code)
	print(resultado.headers['content-type'])

	# Imprime a string pura da resposta
	print(resultado.text)

	if resultado.status_code != 200:
		print('Ocorreu um erro ao realizar a requisição')
		return

	lista = resultado.json()
	for pessoa in lista:
		# CUIDADO!!! Diferente do JavaScript/TypeScript, a forma escrita pessoa.id,
		# pessoa.nome ou pessoa.email não vai funcionar, porque pessoa não é uma classe
		# de verdade que possui esses atributos!
		print(f'\nid: {pessoa["id"]} / nome: {pessoa["nome"]}')

def obterPessoa(id):
	resultado = requests.get("https://academico.espm.br/testeapi/obter/" + str(id))

	# Imprime algumas informações simples da resposta
	print(resultado.status_code)
	print(resultado.headers['content-type'])

	# Imprime a string pura da resposta
	print(resultado.text)

	if resultado.status_code != 200:
		print('Ocorreu um erro ao realizar a requisição')
		return

	pessoa = resultado.json()
	print(f'\nid: {pessoa["id"]} / nome: {pessoa["nome"]}')

def criarPessoa(nome, email):
	pessoa = {
		'nome': nome,
		'email': email
	}

	resultado = requests.post("https://academico.espm.br/testeapi/criar", json=pessoa)
	# Se quisesse os parâmetros em ordem, sem utilizar a facilidade de utilizar o nome do parâmetro:
	# resultado = requests.post("https://academico.espm.br/testeapi/criar", None, pessoa)
	#
	# Ainda, se fosse para enviar pessoa como um form da web, e não como um JSON, bastaria
	# passar a pessoa como segundo argumento (cujo parâmetro se chama data)
	# resultado = requests.post("https://academico.espm.br/testeapi/criar", data=pessoa)
	# ou
	# resultado = requests.post("https://academico.espm.br/testeapi/criar", pessoa)

	# Imprime algumas informações simples da resposta
	print(resultado.status_code)
	print(resultado.headers['content-type'])

	# Imprime a string pura da resposta
	print(resultado.text)

	if resultado.status_code != 200:
		print('Ocorreu um erro ao realizar a requisição')
		return

# O uso desse tipo de instrução é muito comum em Python!
# Quando executamos um arquivo direto pela linha de comando, como
# python exemplo_requisicao.py
# o Python fará com que a variável global __name__ valha '__main__', indicando
# que a execução do programa se deu a partir daquele arquivo, e não de outro.
# Quando o arquivo é importado, __name__ valerá o nome do arquivo sem a extensão
# .py, como 'exemplo_requisicao'
if __name__ == '__main__':
	listarPessoas()
