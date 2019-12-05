import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_html(url):
    page = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    return page


def get_films(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    title_film = [i.find('a').text for i in soup.find_all('div', class_='title _FILM_')]
    info_film = [i.text.rstrip(',') for i in soup.find_all('li', class_='film_info_first')]
    link_film = [('https://www.kinopoisk.ru/film/' + (i.find('a').get('href')).split('/')[2] + '/afisha/city/1/')
                 for i in soup.find_all('div', class_='title _FILM_')]
    dict_films = list(zip(title_film, info_film, link_film))
    print(*dict_films, sep='\n')


def get_price_film(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    price = [i.text for i in soup.find_all('span', class_='schedule-item__price')]
    time_ = [i.text for i in soup.find_all('span', class_='schedule-item__template')]
    link = ['fix it!']
    session = list(zip(price, time_, link))
    print(*session, sep='\n')


def main():
    get_films(get_html('https://www.kinopoisk.ru/afisha/city/1/sort_by/count/#sort'))
    get_price_film(get_html('https://www.kinopoisk.ru/film/1188529/afisha/city/1/day_view'))


if __name__ == '__main__':
    main()

'''''
<a href="javascript:;" class="all js-yaticket-button js-metrika-yaticket-button" data-film-id="903831" data-session-id="42686490">10:05</a>
'''''