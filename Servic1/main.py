from flask import Flask, render_template, request, redirect, flash, url_for
import requests
import sqlite3


app = Flask(__name__)


#конектимся к базе данных в данном случае с названием list of clients
db = sqlite3.connect('list of clients', check_same_thread=False)
#для работы с базой данных
sql = db.cursor()
#создание базы данных users объявления её столбцов и опредления информации, которая будет содерджаться в них
sql.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    USD BIGINT,
    КабачокCoin BIGINT,
    BTC BIGINT,
    ETH, BIGINT
)""")
#Сохранения наших изменений в нашей базе данных, обязательно всегда!!!!
db.commit()


@app.route('/create-user', methods=['POST', 'GET'])
def create_user():
    if request.method == "POST":

        user = request.form['user']
        password = request.form['password']

        sql.execute(f"SELECT login FROM users WHERE login = '{user}'")
        # если такого логина нет в таблице
        if sql.fetchone() is None:
            # добавляем в таблицу в первую колонку переменные user_login, user_password и начальный balance
            sql.execute(f'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', (user, password, 100000000, 0, 0, 0))
            db.commit()
            flash('Вы зарегистрирвались', category='success')
            return redirect('/user')
        else:
            print('Такой логин уже занят, зарегестрируйтесь или авторизуйтесь')
            flash("Ошибка в отправке", category='error')
            return render_template("create-user.html")
    else:
        return render_template("create-user.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        course = requests.get('http://192.168.0.8:8777/').text
        print(course)
    return render_template("home.html")


@app.route('/user', methods=['POST', 'GET'])
def about():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        #берём столбцы login, password из таблице users, если  login= ввёденому значения в поле логин на сайте и password = ввёденому значения в поле пароль на сайте
        sql.execute(f"SELECT login, password FROM users WHERE login = '{user}' and password ='{password}'")
        # если такого логина нет отправляем на регестрацию или предлагаем ввести снова его дальше проверяем пароль
        if sql.fetchone() is None:
            return render_template("user.html")
        else:
            user = request.form['user']
            return redirect(url_for('PersonalCabinet', user=user))
    else:
        return render_template("user.html")


@app.route('/personal-cabinet/<path:user>', methods=['POST', 'GET'])
def PersonalCabinet(user):
    return render_template("personal-cabinet.html")


@app.route('/КабачокCoin',  methods=['POST', 'GET'])
def КабачокCoin():
    if request.method == "GET":
        url = request.args.get('url')
        url = 'http://' + url
        #cource = requests.get('http://127.0.0.1:8777/').text
        cource = requests.get(url).text
        print(cource)
    return render_template("КабачокCoin.html", cource=cource)


@app.route('/BTC',  methods=['POST', 'GET'])
def BTC():
    if request.method == "GET":
        url = request.args.get('url')
        url = 'http://' + url
        #cource = requests.get('http://127.0.0.1:8777/').text
        cource = requests.get(url).text
        print(cource)
    return render_template("BTC.html", cource=cource)


@app.route('/ETH',  methods=['POST', 'GET'])
def ETH():
    if request.method == "GET":
        url = request.args.get('url')
        url = 'http://' + url
        #cource = requests.get('http://127.0.0.1:8777/').text
        cource = requests.get(url).text
        print(cource)
    return render_template("ETH.html", cource=cource)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True, host="0.0.0.0", port=8776)