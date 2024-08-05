import requests
import mysql.connector
from bs4 import BeautifulSoup


res =  res = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(res.text, 'html.parser')


names = soup.find_all('h3')
country_name = list()
for name in names:
    country_name.append(name.text.strip())



vals = soup.find_all('div', class_='country-info')
capital = list()
population = list()
area = list()
for val in vals:
    capital.append(val.find(class_='country-capital').text)
    population.append(val.find(class_='country-population').text)
    area.append(val.find(class_='country-area').text)

cnx = mysql.connector.connect(user='root', password='Hosein13811234', host='127.0.0.1', database='Scrapethissite')
cursor = cnx.cursor()
for i in range(len(country_name)):
    cursor.execute('INSERT IGNORE INTO country (Name, Capital, Population, Area) VALUES (%s, %s, %s, %s)', (country_name[i], capital[i], population[i], area[i]))
cnx.commit()
cnx.close()

