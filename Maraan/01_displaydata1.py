import mysql.connector

# Database connection configuration
config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',  # or your database host
    'database': 'ecommerce'
}

try:
    # Establishing the connection
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Executing a query
    query = "SELECT * FROM db_products"  # Change this to your SQL query
    cursor.execute(query)

    # Fetching the results
    results = cursor.fetchall()

    # Printing the results
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()