from flask import Flask, request, render_template, redirect
import pyodbc

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
                          'SERVER=productcatalogue-sqlserver.database.windows.net;'
                          'ProductCatalogueDB;'
                          'UID=assignment;'
                          'PWD=cloudcomputing@123')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')  # Assuming 'products' is your table name
    products = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)