import requests
from bs4 import BeautifulSoup


url = 'https://www.shutterstock.com/search/austin%2C+texas'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('img')
for image in images:
    link = image['src']
    print(link)
