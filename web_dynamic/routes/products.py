from flask import Blueprint, render_template
import mysql.connector

from web_dynamic.app import get_cart_count
from web_dynamic.config import db_config

bp = Blueprint('products', __name__)


@bp.route('/products')
def products():
    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Retrieve product data from the database
    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Render the template and pass the product data to it
    cart_count = get_cart_count()
    return render_template('shop.html', products=products, cart_count=cart_count)
