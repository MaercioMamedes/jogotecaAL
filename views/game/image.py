from main import app
from flask import send_from_directory, request


@app.route('/medias/<file_name>')
def image(file_name):
    return send_from_directory('medias', file_name)
