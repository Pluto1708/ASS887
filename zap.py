from flask import Flask, render_template, request, redirect, url_for
import pyodbc

# Initialize Flask app
app = Flask(__name__)

# Azure SQL Database connection details
server = 'productcatalogue-sqlserver.database.windows.net'
database = 'ProductCatalogueDB'
username = 'assignment'
password = 'cloudcomputing@123'

# Set up the database connection
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      f'UID={username};'
                      f'PWD={password}')
cursor = conn.cursor()

# Route to the homepage
@app.route('/')
def home():
    return "Welcome to the Product Catalogue App!"

# Route to add new products
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Get data from the form
        product_name = request.form['product_name']
        product_description = request.form['product_description']
        product_price = request.form['product_price']

        # Insert product into database
        cursor.execute("INSERT INTO Products (product_name, product_description, product_price) VALUES (?, ?, ?)",
                       (product_name, product_description, product_price))
        conn.commit()

        # Redirect to the list of products
        return redirect(url_for('list_products'))

    return render_template('add_product.html')

# Route to list all products
@app.route('/products')
def list_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return render_template('list_products.html', products=products)

# Route for product search
@app.route('/search', methods=['GET', 'POST'])
def search_product():
    if request.method == 'POST':
        # Get the search query from the form
        query = request.form['q']
        
        # Query the database to find matching products
        cursor.execute("SELECT * FROM Products WHERE product_name LIKE ?", ('%' + query + '%',))
        products = cursor.fetchall()
        
        return render_template('search_results.html', products=products, query=query)
    
    return render_template('search.html')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5002)