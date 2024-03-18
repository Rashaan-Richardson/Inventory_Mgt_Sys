from flask import Flask, render_template
import sqlite3

# Create a Flask app
app = Flask(__name__)

# Define a route and its handler function
@app.route('/')
def index():
    return 'We are connected!'

def get_db_connection():
    conn = sqlite3.connect('IMS.db')
    conn.row_factory = sqlite3.Row
    print('database opened')
    return conn

@app.route('/products')
def display_products():
    conn = get_db_connection()
    c = conn.execute('SELECT * FROM Products')
    products = c.fetchall()
    conn.close()
    print(products)
    return render_template('products.html', products=products)

@app.route('/transactions')
def display_transactions():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM Transactions')
    transactions = cursor.fetchall()
    conn.close()
    return render_template('transactions.html', transactions=transactions)

@app.route('/suppliers')
def display_suppliers():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM Suppliers')
    suppliers = cursor.fetchall()
    conn.close()
    return render_template('suppliers.html', suppliers=suppliers)

@app.route('/orders')
def display_orders():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM Orders')
    orders = cursor.fetchall()
    conn.close()
    return render_template('orders.html', orders=orders)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

