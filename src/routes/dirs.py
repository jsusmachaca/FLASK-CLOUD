from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required
import os
from config.config import Path

dirs_bp = Blueprint('dirs', __name__)


@dirs_bp.route('/home/<dir>')
@login_required
def dirs(dir):
    os.chdir(Path.dir_path + dir)
    print("DIR? ==>")
    files = [content for content in os.listdir() if os.path.isfile(content) == True]
    dirs = [content for content in os.listdir() if os.path.isdir(content) == True]
    current = os.getcwd()[1:]
    print(current)
    fst = {
        'dirs': dirs,
        'files': files,
        'current': current,
    }
    print("actual ===>",os.getcwd())
    return render_template('index.html', fs=fst)