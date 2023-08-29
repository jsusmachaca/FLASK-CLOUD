from flask import Blueprint, send_file
from config.config import Path


downld_dp = Blueprint('download', __name__)

@downld_dp.route('/download/<filename>', methods=['GET'])
def down(filename):
    return send_file(Path.dir_path + filename, as_attachment=filename)
