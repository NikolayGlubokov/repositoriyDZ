from flask import Flask, render_template, url_for


menu = [
    {'name':'Главная', 'url':'index'},
    {'name':'О нас', 'url': 'about'},
    {'name':'Обратная связь', 'url':'contact'}]
app = Flask(__name__)
@app.route('/index')
@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html',title='Главная', menu=menu)

@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='описание сайта', menu=menu)

@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"

if __name__=='__main__':
    app.run(debug=True)