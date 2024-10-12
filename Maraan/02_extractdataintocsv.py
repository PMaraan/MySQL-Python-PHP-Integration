import mysql.connector
import csv

# Database connection configuration
config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',  # or your database host
    'database': 'ecommerce'
}

# CSV file name
csv_file = 'output.csv'

try:
    # Establishing the connection
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Executing a query
    query = "SELECT * FROM db_products"  # Change this to your SQL query
    cursor.execute(query)

    # Fetching column names
    columns = [column[0] for column in cursor.description]

    # Fetching all rows
    rows = cursor.fetchall()

    # Writing to CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Writing the header
        writer.writerow(columns)
        
        # Writing the data
        writer.writerows(rows)

    print(f"Data has been written to {csv_file} successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()