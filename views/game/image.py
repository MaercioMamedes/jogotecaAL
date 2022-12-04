from main import app
from flask import send_from_directory, request


"""view para incorporar imagens de upload no HTML"""
@app.route('/medias/<file_name>')
def image(file_name):
    return send_from_directory('medias', file_name)
