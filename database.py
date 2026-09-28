import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",      # Yahan apna MySQL password likhna hai
        database="restaurant_management"
    )

    if connection.is_connected():
        print("✅ Connected to MySQL Database Successfully!")

except mysql.connector.Error as error:
    print("❌ Error:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔒 Connection Closed.")