#notes web-scrapping

from bs4 import BeautifulSoup

with open('home.html' , 'r') as html_file:
    content = html_file.read()
    

    soup = BeautifulSoup(content , 'lxml')
    # print(soup.prettify())
    # tag = soup.find_all('h1')
    # table_columns = soup.find_all('td')

    # for td in table_columns:
    #     print(td.text)

    price = soup.find_all('tr' , class_="price")
   
    for p in price:
        pri = price.td.text.split()[-1]
        #print(pri)
        print(f'{pri}')

