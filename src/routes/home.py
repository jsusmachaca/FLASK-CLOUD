from flask import redirect, url_for, render_template, Blueprint
from flask_login import login_required
import os

from config.config import Path

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    os.chdir(Path.dir_path)
    files = [content for content in os.listdir() if os.path.isfile(content) == True]
    directories = [content for content in os.listdir() if os.path.isdir(content) == True]

    filesystem = {
        'directories': directories,
        'files': files,
        'current_path': Path.dir_path[1:]
    }
    return render_template('index.html', fs=filesystem)
