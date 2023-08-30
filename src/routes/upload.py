from flask import request, redirect, url_for, Blueprint
from flask_login import login_required
from config.config import Path


up_bp = Blueprint('upload', __name__)


@up_bp.route('/upload/<path:args>', methods=['POST'])
@login_required
def upload(args):
    file = request.files.get('file')    
    print(file.filename)
    file.save('/' + args + '/' + file.filename)
    print(f'Saving file in => /{args}/{file.filename}')
    return redirect(url_for('home.home'))
