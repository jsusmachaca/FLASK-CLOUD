from flask import Blueprint, redirect, url_for, render_template, request
import os
from config.config import Path

dirs_bp = Blueprint('dirs', __name__)


@dirs_bp.route('/home/<path:args>')
def dirs(args):
    os.chdir(Path.dir_path + args)
    files = os.listdir()
    fst = {
        'dirs': files,
        'files': 'Pepep'
    }
    return render_template('index.html', fs=fst)