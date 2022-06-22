import sqlite3
import os
from flask import Flask, g, render_template, url_for, request, flash, session, redirect, abort
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBUG=True
SEKRET_KEY ='e888404975e35a13977afc3e68925e093b101fa6'








# menu = [
#     {'name':'Главная', 'url':'index'},
#     {'name':'О нас', 'url': 'about'},
#     {'name':'Обратная связь', 'url':'contact'}]
app = Flask(__name__)
app.config.from_object(__name__)


app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db=connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/index')
@app.route("/")
def index():
    db=get_db()
    dbase=FDataBase(db)
    # print(url_for('index'))
    return render_template('index.html',title='Главная', menu=dbase.get_menu())

@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='описание сайта', menu=[])

@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method=='POST':
        if len(request.form['username'])>2:
            flash('Сообщение отправлено успешно', category='success')
        else:
            flash('Ошибка отправки данных', category='error')
        # print(request.form)
        # context = {
        #     'username':request.form['username'],
        #     'email':request.form['email'],
        #     'message': request.form['message']
        # }
    return render_template('contact.html', title='Обратная связь',menu=[])

@app.route("/profile/<path:username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Пользователь: {username}"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html',
title='Страница не найдена', menu=[])

@app.route('/login', methods=['POST','GET'])
def login():
    if 'userLogged' == session:
        return redirect(url_for('profle', username=session['userLogged']))
    elif request.method == "POST" and request.form ['username'] =='Nikolay' and request.form['password'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=[])






















if __name__=='__main__':
    app.run(debug=True)