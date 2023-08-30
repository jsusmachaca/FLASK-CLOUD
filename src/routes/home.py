from flask import redirect, url_for, render_template, Blueprint
from flask_login import login_required
import os

from config.config import Path

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
@home_bp.route('/home/')
def none():
    return redirect(url_for('home.home'))

@home_bp.route('/home')
@login_required
def home():
    os.chdir(Path.dir_path)
    data = os.listdir()
    files = []
    dirs = []
    for content in data:
        if os.path.isdir(content) == True:
            dirs.append(content)
        else:
            files.append(content)

    filesys = {
        'dirs': dirs,
        'files': files,
    }
    return render_template('index.html', fs=filesys)
