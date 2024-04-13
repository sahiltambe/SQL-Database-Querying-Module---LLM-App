import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Execute a query to fetch all records from the table
cursor.execute("SELECT * FROM student")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Define the CSV file name
csv_file = "students.csv"

# Write the fetched rows to a CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])  # Write headers
    writer.writerows(rows)  # Write rows

# Close the database connection
conn.close()

print(f"Data has been successfully exported to {csv_file}.")
