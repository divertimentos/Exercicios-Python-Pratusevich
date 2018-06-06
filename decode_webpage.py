from bs4 import BeautifulSoup
import requests


url = "http://pudim.com.br"
r = requests.get(url)
r_html = r.text
# print(r_html)

soup = BeautifulSoup(r_html, "html.parser")
title = soup.find('span', 'articletitle').string

# Deu erro nesse código.