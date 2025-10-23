from jinja2 import Template


# 1

# html = '''
# {% macro input_func(name, placeholder, type='text' ) %}
# <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
# {% endmacro %}
#
# <p>{{ input_func('firstname', 'Имя') }}</p>
# <p>{{ input_func('lastname', 'Фамилия') }}</p>
# <p>{{ input_func('address', 'Адрес') }}</p>
# <p>{{ input_func('phone', 'Телефон', type='tel') }}</p>
# <p>{{ input_func('email', 'Почта', type='email') }}</p>
#
# '''
#
# tm = Template(html)
# msg = tm.render()
# print(msg)


# 2

punkt = [
    {'href': '/index', 'pun': 'Главная'},
    {'href': '/news', 'pun': 'Новости'},
    {'href': '/about', 'pun': 'О компании'},
    {'href': '/shop', 'pun': 'Магазин'},
    {'href': '/contacts', 'pun': 'Контакты'}
]

link = '''
<ul>
    {% for p in punkt %}
        {% if p.pun == 'Главная' %}
            <li><a href='{{ p.href }}' class='active'>{{ p.pun }}</a></li>
        {% else %}
            <li><a href='{{ p.href }}'>{{ p.pun }}</a></li>
        {% endif %}
    {% endfor %}
</ul>
'''


tm = Template(link)
msg = tm.render(punkt=punkt)
print(msg)
