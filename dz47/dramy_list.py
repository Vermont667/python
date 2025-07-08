from bs4 import BeautifulSoup
import requests
import csv


class Drams:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        drams = self.html.find_all('article')
        for item in drams:
            name = item.find('div', class_='card__title').text
            rating = item.find('div', class_='card__rating-ext-count').text
            year = item.find('li').text.replace('\n', '').split(':')[1].strip()
            transl = item.find_all('li')[1].text.replace('\n', '').split(':')[1].strip()
            genre = item.find_all('li')[3].text.replace('\n', '').split(':')[1].strip()
            try:
                series = item.find_all('li')[4].text.replace('\n', '').split(':')[1].strip()
            except IndexError:
                series = '0'
            status = item.find('a', class_='card__img').text.strip()
            url = item.find('a')['href']
            self.res.append({
                'name': name,
                'rating': rating,
                'year': year,
                'transl': transl,
                'genre': genre,
                'series': series,
                'status': status,
                'url': url
            })
        print(self.res)

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f'Дорама №{i}\n\nНазвание: {item['name']}'
                        f'\nРейтинг: {item['rating']}'
                        f'\nГод: {item['year']}'
                        f'\nПеревод: {item['transl']}'
                        f'\nЖанр: {item['genre']}'
                        f'\nСерий: {item['series']}'
                        f'\nСсылка: {item['url']}\n\n{'*' * 40}\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()





