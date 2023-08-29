from flask import redirect, url_for, flash, render_template, Blueprint
from flask import request, session
from database.database import con
from models.User import User


login_bp = Blueprint('login', __name__)
mysql = con()

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home.home'))
    else:
        if request.method == 'POST':
            name = request.form.get('name')
            passwd = request.form.get('password')
            with mysql.cursor() as cur:
                cur.execute('SELECT * FROM users WHERE username="%s"' %(name))
                row = cur.fetchone()

            if row != None:
                user = User(row[0], row[1], name, User.showPassword(row[3], passwd))
                
                if user.password:
                    session['username'] = name
                    return redirect(url_for('home.home'))
                else:
                    flash('Wrong Password')
                    return redirect(url_for('login.login'))
            else:
                flash('User not found')
                return redirect(url_for('login.login'))
            
        else:
            return render_template('auth/login.html')