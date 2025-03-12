import pyodbc  

# Azure SQL Database details  
server = 'productcatalogue-sqlserver.database.windows.net'  
database = 'ProductCatalogueDB'  
username = 'assignment'  # Your Azure SQL username  
password = 'cloudcomputing@123'  # Replace with your actual password  
driver = '{ODBC Driver 18 for SQL Server}'  # Ensure this driver is installed  

# Connection string  
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:  
    conn = pyodbc.connect(conn_str)  
    print("Connection to Azure SQL Database successful!")  
    
    # Test a simple query  
    cursor = conn.cursor()  
    cursor.execute("SELECT @@VERSION")  
    row = cursor.fetchone()  
    print("Database Version:", row[0])  
    
    conn.close()  
except Exception as e:  
    print("Error:", e)  