import requests
import time
from bs4 import BeautifulSoup
from csv import writer

lista= []
kategorije=[]
br = 1

url_file = open('linkoviTest.txt','r')
for url in url_file.readlines():
    lista.append(url)
url_file.close()

lista_links = [x[:-1] for x in lista]

kat_file = open('kategorijeTest.txt','r')
for kat in kat_file.readlines():
    kategorije.append(kat)
kat_file.close()

lista_kat = [x[:-1] for x in kategorije]

with open('scrap_dataTest.csv', 'w', encoding='UTF-8', newline="") as csv_file:
    csv_writer = writer(csv_file)
    headers = ['ID','Link','Title','Kategorije','Date','Text', 'Author']
    csv_writer.writerow(headers)

    for urls in lista_links:

        response = requests.get(urls)
        b_soup = BeautifulSoup(response.text, 'html.parser')
        posts = b_soup.select('body')

        for script in b_soup(["script", "style"]):
            script.decompose()

        for post in posts:
            link = urls
            title=post.find('h2').get_text()
            date = post.find('time').get_text()
            text = post.find('div',attrs={'itemprop':"articleBody"}).get_text()
            author = post.find('span', attrs={'itemprop':"name"}).get_text()
            csv_writer.writerow([br, link, title, lista_kat[br-1], date, text, author])

        br = br + 1
    time.sleep(5)