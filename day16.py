#Web Scrapping
import requests
from bs4 import BeautifulSoup

url = 'https://realpython.com'  
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.find_all('h2')

for title in titles:
    print(title.get_text())

