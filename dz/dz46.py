
from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('doramy.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow([data["name"], data["rating"], data["description"]])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find('div', id='dle-content')
    dorams = p1.find_all('article')
    for doram in dorams:
        name = doram.find('div', class_='card__title').text
        rating = doram.find('div', class_='card__rating-ext-count centered-content').text
        description = doram.find('p', class_='card__text line-clamp').text

        data = {'name': name, 'rating': rating, 'description': description}
        write_csv(data)


def main():
    url = 'https://kdramy.online/bl-lakorny/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()