import mysql.connector


def place_order():
    try:
        # ================= DATABASE CONNECTION =================

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="restaurant_management"
        )

        cursor = connection.cursor()

        # ================= AVAILABLE MENU =================

        print("\n========== AVAILABLE MENU ==========")

        cursor.execute("SELECT * FROM menu")
        menu = cursor.fetchall()

        print("ID\tFood Name\tCategory\tPrice")
        print("-" * 60)

        for item in menu:
            print(
                f"{item[0]}\t"
                f"{item[1]}\t\t"
                f"{item[2]}\t\t"
                f"₹{item[3]}"
            )

        print("-" * 60)

        # ================= CUSTOMERS =================

        print("\n========== CUSTOMERS ==========")

        cursor.execute("""
            SELECT customer_id, customer_name, phone_number, table_number
            FROM customer
        """)

        customers = cursor.fetchall()

        print("ID\tName\t\tPhone\t\tTable")
        print("-" * 60)

        for customer in customers:
            print(
                f"{customer[0]}\t"
                f"{customer[1]}\t\t"
                f"{customer[2]}\t\t"
                f"{customer[3]}"
            )

        print("-" * 60)

        # ================= CUSTOMER ID =================

        customer_id = int(input("Enter Customer ID: "))

        # Check Customer ID

        cursor.execute(
            "SELECT customer_id FROM customer WHERE customer_id = %s",
            (customer_id,)
        )

        customer = cursor.fetchone()

        if customer is None:
            print("❌ Invalid Customer ID!")
            cursor.close()
            connection.close()
            return

        # ================= CART =================

        cart = []
        grand_total = 0

        while True:

            print("\n------------------------------")

            food_id = int(input("Enter Food ID: "))
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("❌ Quantity must be greater than 0!")
                continue

            # ================= CHECK FOOD =================

            cursor.execute(
                "SELECT food_name, price FROM menu WHERE food_id = %s",
                (food_id,)
            )

            food = cursor.fetchone()

            if food is None:
                print("❌ Invalid Food ID!")
                continue

            food_name = food[0]
            price = float(food[1])

            total_price = price * quantity

            # ================= ADD TO CART =================

            cart.append(
                (
                    food_id,
                    food_name,
                    quantity,
                    price,
                    total_price
                )
            )

            grand_total += total_price

            print(f"✅ {food_name} added to cart!")

            more = input("\nAdd More Items? (Y/N): ").lower()

            if more != "y":
                break

        # ================= BILL =================

        print("\n")
        print("=" * 45)
        print("                 BILL")
        print("=" * 45)

        for item in cart:

            food_id = item[0]
            food_name = item[1]
            quantity = item[2]
            price = item[3]
            total_price = item[4]

            print(
                f"{food_name:15} "
                f"x{quantity:<3} "
                f"₹{total_price:.2f}"
            )

            # ================= SAVE ORDER =================

            cursor.execute(
                """
                INSERT INTO orders
                (customer_id, food_id, quantity, total_price)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    customer_id,
                    food_id,
                    quantity,
                    total_price
                )
            )

        connection.commit()

        # ================= FINAL BILL =================

        print("-" * 45)
        print(f"Grand Total : ₹{grand_total:.2f}")
        print("=" * 45)

        print("✅ Order Placed Successfully!")

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Database Error:", error)

    except ValueError:
        print("❌ Please Enter Valid Numbers Only!")