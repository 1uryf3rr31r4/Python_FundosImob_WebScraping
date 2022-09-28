import requests
from bs4 import BeautifulSoup

site = "https://www.fundsexplorer.com.br/funds/mxrf11"

html = requests.get(site).content

dados = BeautifulSoup(html, 'html.parser')

preco = dados.find("span", class_ = "price")
ultimo_rendimento = dados.find_all("span", class_ = "indicator-value")

print("Preço:", preco.text[19:])
print("Último Rendimento:", ultimo_rendimento[1].text[17:])