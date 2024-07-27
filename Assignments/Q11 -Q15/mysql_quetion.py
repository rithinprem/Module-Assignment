import pandas as pd
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rithin@2000',
    database='travel_planner'
)

# Query the bookings table
query = "SELECT * FROM bookings"

# Load the data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display the DataFrame
print(df)
