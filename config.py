import os


"""Parâmetros de configuração de conexão com o Banco de dados MySql"""
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='root',
        password='',
        server='localhost',
        database='jogoteca2'
    )

SECRET_KEY = 'rF1i52H8b5&!'
SQLALCHEMY_TRACK_MODIFICATIONS = False

"""
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_UNIX_SOCKET = "/opt/lampp/var/mysql/mysql.sock"
MYSQL_DB = "GameDataBase"
MYSQL_PORT = 3306
# UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/medias'"""
