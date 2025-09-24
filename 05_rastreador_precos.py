import requests
from bs4 import BeautifulSoup

url = input("Digite a URL do produto: ")
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Exemplo para Amazon (pode variar conforme o site)
preco = soup.find("span", {"class": "a-price-whole"})

if preco:
    print("Preço encontrado:", preco.text)
else:
    print("Não foi possível encontrar o preço. Verifique o seletor HTML.")
