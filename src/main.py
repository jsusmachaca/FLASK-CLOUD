from flask import Flask, redirect, url_for, render_template, flash, request, session
from flask_mysqldb import MySQL
from flask_session import Session
from config.config import Config
from models.User import User

config = Config()

app = Flask(__name__)
app.config.from_object(config)
mysql = MySQL(app)
Session(app)

@app.route('/')
def home():
    return redirect(url_for('index'))
    
@app.route('/home')
def index():
    if 'username' in session:
        print(session['username'])
        print(session)
        return render_template('index.html')
    else:
        return redirect(url_for('sign_in'))

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('password')
        with mysql.connection.cursor() as cur:
            cur.execute('SELECT * FROM users WHERE username="%s"' %(name))
            row = cur.fetchone()

        if row != None:
            user = User(0, name, User.showPassword(row[3], passwd))
            if user.password:
                session['username'] = name
                return redirect(url_for('index'))
            else:
                flash('Wrong Password')
                return redirect(url_for('sign_in'))
        else:
            flash('User not found')
            return redirect(url_for('sign_in'))
        
    else:
        return render_template('auth/sign-in.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sig_in():
    if request.method == 'POST':
        full_name = request.form.get('full-name')
        name = request.form.get('name')
        passwd = request.form.get('password')
        with mysql.connection.cursor() as cur:
            cur.execute('INSERT INTO users(full_name, username, password) VALUES ("%s", "%s", "%s")' %(full_name, name, User.generatePassword(passwd)))
            mysql.connection.commit()

        return redirect(url_for('sign_in'))
        
    else:
        return render_template('auth/sign-up.html')

@app.route('/insert', methods=['POST'])
def insert():
    session.pop('username')
    print(session)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='192.168.1.10', port=8000)