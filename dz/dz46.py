
from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('doramy.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow([data["name"], data["rating"], data["year"], data["transl"],
                         data["genre"], data["series"], data['status'], data["url"]])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find('div', id='dle-content')
    drams = p1.find_all('article')
    for dramy in drams:
        name = dramy.find('div', class_='card__title').text
        rating = dramy.find('div', class_='card__rating-ext-count').text
        year = dramy.find('li').text.replace('\n', '').split(':')[1].strip()
        transl = dramy.find_all('li')[1].text.replace('\n', '').split(':')[1].strip()
        genre = dramy.find_all('li')[3].text.replace('\n', '').split(':')[1].strip()
        try:
            series = dramy.find_all('li')[4].text.replace('\n', '').split(':')[1].strip()
        except IndexError:
            series = []
        status = dramy.find('a', class_='card__img').text.strip()
        url = dramy.find('a').get('href')
        data = {'name': name, 'rating': rating, 'year': year, 'transl': transl,
                'genre': genre, 'series': series, 'status': status, 'url': url}
        write_csv(data)


def main():
    for i in range(1, 10):
        url = f'https://kdramy.online/bl-lakorny/page/{i}/'
        get_data(get_html(url))


if __name__ == '__main__':
    main()