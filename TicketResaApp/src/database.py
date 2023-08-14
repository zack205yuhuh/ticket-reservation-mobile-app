import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=82,
    user="root",
    password="zakaria10")

# Close connection
cnx.close()
