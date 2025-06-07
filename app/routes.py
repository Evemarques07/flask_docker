from flask import Blueprint, render_template
from . import mysql

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, price FROM products")
    data = cur.fetchall()
    cur.close()
    return render_template('products.html', products=data)
