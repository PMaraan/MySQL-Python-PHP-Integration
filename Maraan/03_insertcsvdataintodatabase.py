import mysql.connector
import csv

# Database connection configuration
config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',  # or your database host
    'database': 'ecommerce2'
}

# CSV file name
csv_file = 'output.csv'  # Change this to your CSV file name

try:
    # Establishing the connection
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Reading the CSV file
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        
        # Assuming the first row is the header
        header = next(reader)
        
        # Preparing the insert statement
        placeholders = ', '.join(['%s'] * len(header))  # Create a placeholder string
        query = f"INSERT INTO products ({', '.join(header)}) VALUES ({placeholders})"

        # Inserting each row from the CSV file
        for row in reader:
            cursor.execute(query, row)

    # Committing the transaction
    connection.commit()
    print("Data has been inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()