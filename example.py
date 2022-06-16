from jinja2 import Template, Environment, FileSystemLoader

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per=Person("Игорь", 28)
#
#
#
# # per={'name':'Игорь','age':28}
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
# {# #} блок комментариев
# # ## Строчный коментарий
# {% for <выражение>%}
# <повторяемый фрагмент>
# {% endfor%}

# data= "{% raw %} Строка, с названием {{ name }}. Со значением {% endraw %}" # Спецификатор шаблона
# tm = Template(data)
# msg = tm.render(name='Игорь')
#
# print(msg)
#
#
# link = "<a href='#'> Ссылка </a>"
# tm = Template ("{{ link | e}}")
# msg = tm.render(link=link)
#
# print(msg)
#
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Ростов'},
#     {'id': 3, 'city': 'Рязань'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'}
# ]

# link = """
# <select name='cities'>
#     {% for  c in cities %}
#     <option value='{{c.id}}'>{{c.city}}</option>
#     {% endfor %}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)
#
# link = """
# <select name='cities'>
#     {% for  c in cities -%}
#     {% if c.id >3 -%}
#         <option value='{{c.id}}'>{{c.city}}</option>
#     {% elif c.city=='Москва'%}
#         <option>{{c.city}}</option>
#     {% else%}
#         {{ c.city }}
#     {% endif %}
#     {% endfor %}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)
#
# data=[
#     {'href': 'index', 'title':'Главная'},
# {'href': 'news', 'title':'Новости'},
# {'href': 'about', 'title':'О компании'},
# {'href': 'shop', 'title':'Магазин'},
# {'href': 'contacts', 'title':'Контакты'},
# ]
#
# d="class = 'active'"
# link="""
# <ul>
# {% for di in data-%}
# {% if di.href=="index"-%}
#     <li><a href="/{{di.href}} {{d}}>{{di.title}}</a></li>
# {% else%}
#     <li><a href="/{{di.href}}>{{di.title}}</a></li>
# {%endif-%}
# {%endfor-%}
# </ul>
#
# """
# tm = Template(link)
# msg = tm.render(data=data, d=d)
# print(msg)

# lst = [1, 2, 3, 4, 5, 6]
# tpl="Cумму: {{cs | sum}} "
#
# cars=[
#     {'model':'Audi','price':23000},
# {'model':'Skoda','price':17300},
# {'model':'Renault','price':44300},
# {'model':'BMW','price':50000}
#
# ]

# # tpl="Сумма: {{ (cs | min(attribute='price')).model}}"
# tpl="Сумма: {{ cs | replace('model', 'brand')}}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# person=[
#     {'name':'Aleksey', 'year': 18, 'weight': 78.5},
#     {'name': 'Nikita', 'year': 28, 'weight': 82.3},
#     {'name': 'Vitaliy', 'year': 33, 'weight': 94.0}
# ]
#
# tpl="""
# {%- for u in users -%}
# {% filter string %} {{ u.name }} - {{u.weight}} {% endfilter %}
# {% endfor -%}
# """
#
# tm = Template(tpl)
# msg = tm.render(users=person)
# print(msg)

# html="""
# {% macro input(name, placeholder, type='text') -%}
#     <input type='{{ type }}' name='{{ name }}' placeholder='{{placeholder}}'>
#
# {% endmacro -%}
#
# <p>{{ input(name='firstname',placeholder= 'Имя') }}</p>
# <p>{{ input(name='lastname', placeholder='Фамилия') }}</p>
# <p>{{ input(name='address', placeholder='Адрес') }}</p>
# <p>{{ input(type='tel', name='phone', placeholder='Телефон')}}</p>
# <p>{{ input(type='email', name='email', placeholder='Почта')}}</p>
#
# """
# person = [
#     {'name': "Алексей", 'year': 18, 'weight': 78.5},
#     {'name': "Никита", 'year': 28, 'weight': 82.3},
#     {'name': "Виталий", 'year': 33, 'weight': 94.0}
# ]
# html = """
# {% macro list_users(list_of_user) -%}
# <ul>
#     {% for u in list_of_user -%}
#     <li> {{u.name}} {{ caller(u)}}</li>
#     {% endfor -%}
# </ul>
# {% endmacro -%}
#
# {% call(user)  list_users(users) %}
# <ul>
#     <li>{{user.year}}</li>
#     <li>{{user.weight}}</li>
# </ul>
#
# {% endcall %}
#
#
# """
#
# tm = Template(html)
# msg = tm.render(users=person)
# print(msg)

person = [
    {'name': "Алексей", 'year': 18, 'weight': 78.5},
    {'name': "Никита", 'year': 28, 'weight': 82.3},
    {'name': "Виталий", 'year': 33, 'weight': 94.0}
]
subs = ['Кльтура','Наука','Политика','Спорт']
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)

print(msg)
