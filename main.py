import requests
from bs4 import BeautifulSoup
import csv
   
URL = "https://www.goodreads.com/quotes"
resp = requests.get(URL)
   
soup = BeautifulSoup(resp.content, 'html5lib')
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'class':'quotes'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'quoteDetails'}):
    quote = {}
    quote['image'] = row.a['href']
    quotes.append(quote)
   
filename = 'quote.csv'
with open(filename, 'w') as f:
    w = csv.DictWriter(f,['image'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)