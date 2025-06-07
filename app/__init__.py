# from flask import Flask
# from flask_mysqldb import MySQL
# import os

# mysql = MySQL()

# def create_app():
#     app = Flask(__name__)
    
#     app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
#     app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
#     app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
#     app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

#     mysql.init_app(app)

#     from .routes import main 
#     app.register_blueprint(main)

#     return app


from flask import Flask
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

load_dotenv()

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'mysql_db' 
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = 'productdb'


    mysql.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app

