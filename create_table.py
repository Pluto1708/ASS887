import pyodbc

# Database connection details
server = 'productcatalogue-sqlserver.database.windows.net'
database = 'ProductCatalogueDB'
username = 'assignment'
password = 'cloudcomputing@123'  # Replace with your actual password

# Connect to Azure SQL
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
)

cursor = conn.cursor()

# Create the Products table if it doesn't exist
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Products')
    BEGIN
        CREATE TABLE Products (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name NVARCHAR(255) NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            description NVARCHAR(MAX)
        )
    END
""")

conn.commit()
print("✅ Products table created (if it didn't already exist).")

# Close connection
cursor.close()
conn.close()