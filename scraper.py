import requests  # type: ignore

from bs4 import BeautifulSoup # type: ignore

import csv

url = 'http://books.toscrape.com/'



resposta = requests.get(url)
resposta.encoding = 'UTF-8'



soup = BeautifulSoup(resposta.text, 'html.parser')

livros = soup.find_all('article', class_='product_pod')



with open('relatorio.csv', 'w', newline='', encoding='UTF=8') as csv_file:
    escritor = csv.writer(csv_file)

    escritor.writerow(['titulo', 'preco','link'])
    for livro in livros:
     titulo = livro.h3.a['title']  #h3=titulo e o a=link
     link = livro.h3.a['href']
     preco = livro.find('p', class_='price_color').text 
     escritor.writerow([titulo, preco, url+link])