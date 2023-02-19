import requests
from bs4 import BeautifulSoup
from csv import writer
import csv
import hashlib

datPoc=[44,5,10,9,4,3]
datKraj=[48,9,14,13,8,7]
#datPoc=[44,5,10,9,4,3]
#datKraj = [1154,374,292,287,175,204]
#dat = [1075, 358, 274, 271, 170, 199, 112] #1075
cat = ['istrain','politika','crna-kronika','gospodarstvo','sport','kultura']
br = len(cat)

for broj in range (0,br):
    for page in range(datPoc[broj],datKraj[broj]):
        print('Page :', page)
        url ='https://www.istrain.hr/index.php/'+cat[broj]+'-arhiva?start='+str(page*4)
        #if(page == 0 & cat==0):
        #   url ='https://www.istrain.hr/index.php/'+cat[broj]+'-arhiva'
        #else:
        #    url ='https://www.istrain.hr/index.php/'+cat[broj]+'-arhiva?start='+str(page*4)
        page = requests.get(url)
        b_soup = BeautifulSoup(page.text, 'html5lib')
        #posts = b_soup.find('div',attrs={'class':"items-more"})
        posts1 =b_soup.find('ol')
        posts2 = posts1.find_all("li")
    
        links =open("linkoviA.csv","a",newline="")
        fieldnames = ["link"]
        writer=csv.DictWriter(links, fieldnames=fieldnames)

        categ = open("kategorijeA.csv","a",newline="")
        fieldnames_k =["kategorije"]
        writer_k=csv.DictWriter(categ, fieldnames=fieldnames_k)

        for post in posts2:
            link= BeautifulSoup(str(post),'html.parser')
            gettinglink= link.find('a',href=True)
            
            writer.writerow({"link":"https://www.istrain.hr"+str(gettinglink['href'])})  
            writer_k.writerow({"kategorije":cat[broj]})

        links.close()
        categ.close()