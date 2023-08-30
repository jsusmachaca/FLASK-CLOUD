from flask import Blueprint, send_file, request
from flask_login import login_required
from config.config import Path


downld_dp = Blueprint('download', __name__)

@downld_dp.route('/download/<path:args>', methods=['POST'])
@login_required
def download(args):
    # Path.dir_path
    file = request.form.get('file')
    print('archivo bro =>', file)
    print('argumentos bro ==>', args)
    return send_file( f'/{args}/{file}', as_attachment='pepe.txt')
