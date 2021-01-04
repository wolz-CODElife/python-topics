'''
This is a web scrapper example, scarping data from a quotes site

'''
#for a start you need two major modules, 
#one to access the web address, by sending requests 
#the other for identifying the HTML syntax
import requests
from bs4 import BeautifulSoup
#url => the address we want to scrape
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quotesTags = tags[i].find_all('a', class_='tag')

    for tag in quotesTags:
        print(tag.text, end='\t')
        print("="*25)
