import pyodbc
import csv

# Database connection parameters
server = 'YourServerName'
database = 'YourDatabaseName'
username = 'YourUsername'
password = 'YourPassword'

# Connect to the SQL Server database
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# Query to extract data from the table
query = "SELECT * FROM YourTableName"

# Execute the query
cursor.execute(query)

# Fetch all results
rows = cursor.fetchall()

# Specify the CSV file path
csv_file_path = 'output.csv'

# Write results to CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the column headers
    writer.writerow([column[0] for column in cursor.description])
    
    # Write the data rows
    writer.writerows(rows)

# Close the database connection
cursor.close()
connection.close()

print(f"Data exported to {csv_file_path} successfully.")
