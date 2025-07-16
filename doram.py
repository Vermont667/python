import csv

def csv_to_html_table(csv_filepath, html_filepath):
    """
    Читает данные из CSV файла и записывает их в HTML таблицу.

    Args:
        csv_filepath (str): Путь к CSV файлу.
        html_filepath (str): Путь для сохранения HTML файла.
    """
    try:
        with open(csv_filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Первая строка - заголовки
            data = list(reader)  # Остальные строки - данные
    except FileNotFoundError:
        print(f"Ошибка: Файл {csv_filepath} не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")
        return

    html_table = '<table border="1">\n'
    # Заголовки
    html_table += '  <thead>\n    <tr>\n'
    for col in header:
        html_table += f'      <th>{col}</th>\n'
    html_table += '    </tr>\n  </thead>\n'

    # Тело таблицы
    html_table += '  <tbody>\n'
    for row in data:
        html_table += '    <tr>\n'
        for cell in row:
            html_table += f'      <td>{cell}</td>\n'
        html_table += '    </tr>\n'
    html_table += '  </tbody>\n'
    html_table += '</table>'

    try:
        with open(html_filepath, 'w', encoding='utf-8') as htmlfile:
            htmlfile.write(html_table)
        print(f"Таблица успешно сохранена в {html_filepath}")
    except Exception as e:
        print(f"Ошибка при записи в HTML файл: {e}")

# Пример использования:
csv_file = 'data.csv'  # Замените на ваш CSV файл
html_file = 'output.html'  # Замените на желаемое имя HTML файла
csv_to_html_table(csv_file, html_file)