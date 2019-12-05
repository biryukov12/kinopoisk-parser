import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://beru.ru/catalog/kofe-v-zernakh/76322/list'
page_url = '?page='

page = requests.get(url, headers={'User-Agent': UserAgent().ie})

soup = BeautifulSoup(page.content, 'html.parser')

pages_count = round(int((soup.find('div', class_='_2StYqKhlBr')).text.split()[4])/24)

for i in range(1, pages_count + 1):
    full_url = url + page_url + str(i)
    print(full_url)

print(pages_count)
