import os
from flask import Flask, render_template, url_for


menu = [
    {'name':'Главная', 'url':'index'},
    {'name':'О нас', 'url': 'about'},
    {'name':'Обратная связь', 'url':'contact'},
    {'name':'Личный кабинет', 'url':'cabinet'}]
app = Flask(__name__)

@app.route('/index')
@app.route("/")
def index():
    return render_template('index.html',title='Главная', menu=menu)

@app.route('/about')
def about():
    return render_template('about.html',title='О нас', menu=menu)

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Обратная связь', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)