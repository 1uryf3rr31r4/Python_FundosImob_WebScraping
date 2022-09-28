import requests
from bs4 import BeautifulSoup

site = "https://www.fundsexplorer.com.br/funds/mxrf11"

html = requests.get(site).content