from flask import request, redirect, url_for, Blueprint
from config.config import Path


up_bp = Blueprint('upload', __name__)

@up_bp.route('/upload', methods=['POST'])
def send():
    file = request.files.get('file')
    print(file.filename)
    file.save(Path.dir_path + file.filename)
    return redirect(url_for('home.home'))
