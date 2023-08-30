from flask import Flask
from flask_login import LoginManager
from config.config import DevConfig, Path
from config.run import run

from models.User import User
from database.database import con

from sys import argv
from os import path

from routes.auth.login import login_bp
from routes.home import home_bp
from routes.upload import up_bp
from routes.download import downld_dp
from routes.dirs import dirs_bp



config = DevConfig()

app = Flask(__name__)
app.config.from_object(config)
login_manager = LoginManager(app)
login_manager.login_view = 'login.login'

@login_manager.user_loader
def load_user(id):
    return User.id_user(con(), id)

  
app.register_blueprint(login_bp)
app.register_blueprint(home_bp)
app.register_blueprint(up_bp)
app.register_blueprint(downld_dp)
app.register_blueprint(dirs_bp)



if __name__ == '__main__':
    run(app, argv, Path, path)