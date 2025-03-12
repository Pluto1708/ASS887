# import pyodbc

# # Database connection details
# server = 'productcatalogue-sqlserver.database.windows.net'
# database = 'ProductCatalogueDB'
# username = 'assignment'
# password = 'cloudcomputing@123'  # Replace with actual password

# # pyodbc connection string
# conn = pyodbc.connect(
#     f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#     f"SERVER={server};"
#     f"DATABASE={database};"
#     f"UID={username};"
#     f"PWD={password};"
#     f"Encrypt=yes;"
#     f"TrustServerCertificate=no;"
#     f"Connection Timeout=30;"
# )

# cursor = conn.cursor()
# print("✅ Successfully connected to the database!")

from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Database connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=productcatalogue-sqlserver.database.windows.net;"
    "DATABASE=ProductCatalogueDB;"
    "UID=assignment;"
    "PWD=cloudcomputing@123;"  # Replace with actual password
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)
cursor = conn.cursor()

# Route to add a new product
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    cursor.execute("INSERT INTO Products (name, price, description) VALUES (?, ?, ?)",
                   (data['name'], data['price'], data.get('description', '')))
    conn.commit()
    return jsonify({"message": "✅ Product added successfully!"})

# Route to list all products
@app.route('/list_products', methods=['GET'])
def list_products():
    cursor.execute("SELECT * FROM Products")
    products = [{"id": row[0], "name": row[1], "price": row[2], "description": row[3]} for row in cursor.fetchall()]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)