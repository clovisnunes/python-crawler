import requests
from bs4 import BeautifulSoup
import csv

urls = [
    'https://www.99freelas.com.br/projects?categoria=web-mobile-e-software',
    'https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&page=2',
    'https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&page=3',
    'https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&page=4',
    'https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&page=5',
    'https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&page=6',
    'https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&page=7',
]

titles = []

for url in urls:
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    titles_per_page = soup.find_all('h1', {'class': 'title'})

    for title in titles_per_page:
        titles.append([title.text.strip(), url + title.find('a').get('href')])

print(titles)

with open('freela_extract.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for row in titles:
        writer.writerow(row)