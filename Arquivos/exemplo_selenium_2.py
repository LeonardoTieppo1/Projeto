# Vamos utilizar o pacote Selenium Python para manipular browsers via código:
# https://selenium-python.readthedocs.io/
#
# Para isso, ele precisa ser instalado via pip (de preferência com o VS Code fechado):
# python -m pip install selenium
#
# Depois de instalar o Selenium Python, é necessário instalar o driver referente
# ao browser que será utilizado:
#
# Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox: https://github.com/mozilla/geckodriver/releases
# Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
#
# Depois de baixar o driver, garantir que ele seja instalado/descompactado em uma
# pasta que pertença ao PATH global do sistema (de preferência com o VS Code fechado).
#
# No Linux, podem ser as pastas /usr/bin, /usr/local/bin ou outra que esteja no PATH.
# Para adicionar outra pasta ao PATH, basta editar o arquivo ~/.bashrc, e adicionar
# uma linha parecida com essa:
# export PATH=/nova/pasta/para/adicionar:${PATH}
#
# No Windows, o PATH pode ser editado clicando com o botão direito sobre o ícone do
# Computador (no Windows Explorer), depois no menu "Propriedades", em seguida "Configurações
# avançadas do sistema" e, por fim, em "Variáveis de Ambiente".
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://teams.microsoft.com')

# Poderia utilizar apenas
# loginfmt = driver.find_element_by_name('loginfmt')
# mas se não encontrasse naquele instante, retornaria None
#
# Se não quiser ficar toda hora utilizando a forma do WebDriverWait
# abaixo, pode executar driver.implicitly_wait(tempo_em_segundos)
# para fazer com que as operações find_xxx sempre esperem
# por aquele tempo, e não que sejam instantâneas!
loginfmt = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.NAME, 'loginfmt'))
)

loginfmt.send_keys('usuario')
loginfmt.send_keys(Keys.RETURN)

# Espera a animação acabar
time.sleep(2)

passwd = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.NAME, 'passwd'))
)

passwd.send_keys('senha')
passwd.send_keys(Keys.RETURN)

# Espera a animação acabar
time.sleep(2)

idBtn_Back = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.ID, 'idBtn_Back'))
)

idBtn_Back.click()

# Para obter o XPath:
# Clique com o botão direito no Chrome, "Inspecionar Elemento", localizar o elemento na aba "Elements",
# clique com o botao direito sobre a tag do elemento na aba "Elements", menu "Copy" e por fim,
# menu "Copy XPath" ou "Copy full XPath"
span_equipes = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.XPATH, "//span[@class='app-bar-text'][text()='Equipes']"))
)
# Obtém o pai (poderia pegar direto o button, e validar seu text, mas é para demonstrar como pegar o
# pai de algum elemento)
botao_equipes = span_equipes.find_element_by_xpath("..")
assert botao_equipes.tag_name == 'button'
botao_equipes.click()

# Espera aparecer o div de alguma equipe na tela
h1_alguma_equipe = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.team-name-text'))
)

todos_h1_equipe = driver.find_elements_by_css_selector('h1.team-name-text')

h1_equipe = None

for h1 in todos_h1_equipe:
	if h1.text == '2021-2 Laboratório Experimental':
		h1_equipe = h1
		break

assert h1_equipe != None

h1_equipe.click()

botao_menu = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'button.team-more-btn'))
)

botao_menu.click()

# Para pegar apenas parte do texto: "//*[contains(text(),'onar membro')]"
menu_adicionar_membro = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.XPATH, "//*[text()='Adicionar membro']"))
)
menu_adicionar_membro.click()

input_nome = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, "div.ts-people-picker input.ts-search-input"))
)

alunos = [ 'Maria', 'João' ]

for nome in alunos:
	input_nome.clear()
	input_nome.send_keys(nome)
	div_resultado = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "div.result-title"))
	)
	input_nome.send_keys(Keys.RETURN)

botao_adicionar_habilitado = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.XPATH, "//button[text()='Adicionar'][not(@disabled)]"))
)
botao_adicionar_habilitado.click()

botao_fechar = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, "//button[@track-summary='Close Add Member'][not(@disabled)]"))
)

botao_fechar.click()

time.sleep(5)

driver.close()
