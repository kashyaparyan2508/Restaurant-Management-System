import mysql.connector


# ================= VIEW MENU =================

def view_menu():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="restaurant_management"
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM menu")
        menu = cursor.fetchall()

        print("\n========== RESTAURANT MENU ==========\n")
        print("ID\tFood Name\tCategory\tPrice")
        print("-" * 50)

        for item in menu:
            print(
                f"{item[0]}\t"
                f"{item[1]}\t\t"
                f"{item[2]}\t\t"
                f"₹{item[3]}"
            )

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Database Error:", error)


# ================= ADD FOOD =================

def add_food():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="restaurant_management"
        )

        cursor = connection.cursor()

        food_name = input("Enter Food Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))

        query = """
        INSERT INTO menu (food_name, category, price)
        VALUES (%s, %s, %s)
        """

        values = (food_name, category, price)

        cursor.execute(query, values)
        connection.commit()

        print("\n✅ Food Item Added Successfully!")

        cursor.close()
        connection.close()

    except ValueError:
        print("❌ Please Enter a Valid Price!")

    except mysql.connector.Error as error:
        print("Database Error:", error)


# ================= UPDATE FOOD =================

def update_food():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="restaurant_management"
        )

        cursor = connection.cursor()

        food_id = int(input("Enter Food ID to Update: "))

        # Check Food ID
        cursor.execute(
            "SELECT * FROM menu WHERE food_id = %s",
            (food_id,)
        )

        food = cursor.fetchone()

        if food is None:
            print("❌ Food ID Not Found!")
            cursor.close()
            connection.close()
            return

        new_price = float(input("Enter New Price: "))

        cursor.execute(
            "UPDATE menu SET price = %s WHERE food_id = %s",
            (new_price, food_id)
        )

        connection.commit()

        print("✅ Food Item Updated Successfully!")

        cursor.close()
        connection.close()

    except ValueError:
        print("❌ Please Enter Valid Numbers Only!")

    except mysql.connector.Error as error:
        print("Database Error:", error)


# ================= DELETE FOOD =================

def delete_food():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="restaurant_management"
        )

        cursor = connection.cursor()

        food_id = int(input("Enter Food ID to Delete: "))

        # Check Food ID
        cursor.execute(
            "SELECT * FROM menu WHERE food_id = %s",
            (food_id,)
        )

        food = cursor.fetchone()

        if food is None:
            print("❌ Food ID Not Found!")
            cursor.close()
            connection.close()
            return

        # Confirmation
        confirm = input(
            "Are you sure you want to delete this food? (Y/N): "
        ).lower()

        if confirm == "y":

            cursor.execute(
                "DELETE FROM menu WHERE food_id = %s",
                (food_id,)
            )

            connection.commit()

            print("✅ Food Item Deleted Successfully!")

        else:
            print("❌ Delete Cancelled!")

        cursor.close()
        connection.close()

    except ValueError:
        print("❌ Please Enter a Valid Food ID!")

    except mysql.connector.Error as error:
        print("Database Error:", error)