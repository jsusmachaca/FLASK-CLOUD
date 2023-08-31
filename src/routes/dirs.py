from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required
import os
from config.config import Path

dirs_bp = Blueprint('dirs', __name__)


@dirs_bp.route('/<path:routes>', methods=['GET', 'POST'])
@login_required
def dirs(routes):
    os.chdir(Path.dir_path + routes)
    files = [content for content in os.listdir() if os.path.isfile(content) == True]
    directories = [content for content in os.listdir() if os.path.isdir(content) == True]

    filesystem = {
        'directories': directories,
        'files': files,
        'routes': routes,
        'current_path': os.getcwd()[1:]
    }
    return render_template('directories.html', fs=filesystem)