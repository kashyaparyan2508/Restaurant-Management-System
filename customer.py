import mysql.connector


def add_customer():
    try:
        # ================= DATABASE CONNECTION =================

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="restaurant_management"
        )

        cursor = connection.cursor()

        # ================= CUSTOMER DETAILS =================

        print("\n========== ADD CUSTOMER ==========")

        customer_name = input("Enter Customer Name: ")
        phone_number = input("Enter Phone Number: ")
        table_number = int(input("Enter Table Number: "))

        # ================= INSERT CUSTOMER =================

        query = """
        INSERT INTO customer
        (customer_name, phone_number, table_number)
        VALUES (%s, %s, %s)
        """

        values = (
            customer_name,
            phone_number,
            table_number
        )

        cursor.execute(query, values)

        connection.commit()

        print("\n✅ Customer Added Successfully!")
        print(f"Customer ID: {cursor.lastrowid}")

        cursor.close()
        connection.close()

    except ValueError:
        print("❌ Please Enter a Valid Table Number!")

    except mysql.connector.Error as error:
        print("Database Error:", error)