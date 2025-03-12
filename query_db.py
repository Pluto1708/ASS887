import pyodbc

# Establish the connection to the database
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
                      'SERVER=productcatalogue-sqlserver.database.windows.net;'
                      'DATABASE=ProductCatalogueDB;'
                      'UID=assignment;'
                      'PWD=cloudcomputing@123')

# Create a cursor to interact with the database
cursor = conn.cursor()

# Example SQL query to fetch data from a table
cursor.execute("SELECT TOP 5 * FROM Products")

# Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()