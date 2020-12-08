"""
Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
"""

import requests
from bs4 import BeautifulSoup

url = "http://brasil.pyladies.com/about"

requisicao = requests.get(url)

# Testando se a conexão funcionou
if requisicao.status_code != 200:
	requisicao.raise_for_status()

#requisicao.encoding = 'utf-8' # Mudar o enconding (acentuação)
html = requisicao.text
soup = BeautifulSoup(html, "html.parser")

html_words = soup.get_text().replace('\n', ' ').lower()

total_words = 0
counter_ladies = 0
words = []
unrepeated_words = []

for html_word in html_words.split():
    total_words += 1
    words.append(html_word)

for word in words:
    if word == 'ladies':
        counter_ladies += 1
    if words.count(word) == 1:
        unrepeated_words.append(word)

print(f'Todas as Palavras da página: {words}\n')
print(f'Palavras que apareceram apenas uma vez: {unrepeated_words}\n')
print(f'Total de vezes que apareceu a palavra ladies: {counter_ladies}')
print(f'Total de palavras: {total_words}')