from flask import Blueprint, send_file, request
from flask_login import login_required
from config.config import Path


downld_dp = Blueprint('download', __name__)

@downld_dp.route('/download/<path:args>', methods=['GET'])
@login_required
def download(args):
    return send_file( f'/{args}', as_attachment='file')
