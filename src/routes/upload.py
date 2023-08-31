from flask import request, redirect, url_for, Blueprint
from flask_login import login_required
from config.config import Path

import os

up_bp = Blueprint('upload', __name__)


@up_bp.route('/upload', methods=['POST'])
@login_required
def upload():
    file = request.files.get('file') 
    save_path = request.form.get('path')   
    saving = os.path.join('/'+save_path, file.filename)
    file.save(saving)
    print(f'Saving file in => {saving}')
    return redirect(url_for('home.home'))
