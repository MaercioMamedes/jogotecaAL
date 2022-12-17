from main import app
from flask import send_from_directory, request


"""view para incorporar imagens de upload no HTML"""
@app.route('/medias/<directory>/<file_name>')
def image(directory, file_name):

    return send_from_directory(f'medias/{directory}', file_name)
