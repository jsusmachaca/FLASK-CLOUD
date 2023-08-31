from sys import argv

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

from config.config import DevConfig, Path
from config.init import init
from models.User import User
from database.database import con

from routes.auth.login import login_bp
from routes.auth.logout import logout_bp
from routes.home import home_bp
from routes.upload import up_bp
from routes.download import downld_dp
from routes.dirs import dirs_bp


app = Flask(__name__)

config = DevConfig()
app.config.from_object(config)

login_manager = LoginManager(app)
csrf = CSRFProtect()
login_manager.login_view = 'login.login'


@login_manager.user_loader
def load_user(id):
    return User.id_user(con(), id)

  
app.register_blueprint(login_bp)
app.register_blueprint(home_bp)
app.register_blueprint(dirs_bp)
app.register_blueprint(up_bp)
app.register_blueprint(downld_dp)
app.register_blueprint(logout_bp)

init_app = init(app, argv, Path)

if __name__ == '__main__':
    csrf.init_app(app)
    init_app.run(host='0.0.0.0')