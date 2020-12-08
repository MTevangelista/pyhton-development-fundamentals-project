"""
Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.
"""

import requests
from bs4 import BeautifulSoup

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

requisicao = requests.get(url)

# Testando se a conexão funcionou
if requisicao.status_code != 200:
	requisicao.raise_for_status()

#requisicao.encoding = 'utf-8' # Mudar o enconding (acentuação)
html = requisicao.text
soup = BeautifulSoup(html, "html.parser")

html_informations = []
words = []
regions = ['DF', 'GO', 'MT', 'MS']

uf = str(input("Informe uma sigla de um estado da região Centro-Oeste:\n")).upper()

while uf not in regions:
	print('Região inválida, informe uma nova siga!')
	uf = str(input("Informe uma sigla de um estado da região Centro-Oeste:\n")).upper()

for div_line in soup.find_all('div', class_='linha'):
	replaced_word = div_line.text.replace('\n', ' ')
	html_informations.append(replaced_word)

for html_info in html_informations:
	if uf in html_info:
		print(html_info)
 