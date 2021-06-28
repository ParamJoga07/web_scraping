

from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://coinmarketcap.com/rankings/exchanges/"
html = requests.get(url)
soup = BeautifulSoup(html.content, 'lxml')
companies = soup.find_all('tr')



with open('LINKS4.csv', 'w', newline='', encoding='utf8') as f:
    thewriter = writer(f)
    header = ['NAME', 'LINK']
    thewriter.writerow(header)
    for company in companies:
        name = company.find('a', class_='cmc-link')
        if name:
            name = company.find('a', class_='cmc-link').text
            href1 = company.find('a', class_='cmc-link').get('href')
            link1 = 'https://coinmarketcap.com' + str(href1)
            page_html = requests.get(link1)
            soup2 = BeautifulSoup(page_html.content, 'lxml')
            try:
                weblink = soup2.find('ul', class_='uxo8xk-0 jlcQeb cmc-details-panel-links').a.get('href')
            except AttributeError as a:
                print(name)
                
            links = [name, weblink]
            thewriter.writerow(links)
