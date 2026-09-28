from menu import view_menu, add_food, update_food, delete_food
from customer import add_customer
from order import place_order


while True:
    print("\n========== RESTAURANT MANAGEMENT SYSTEM ==========")
    print("1. View Menu")
    print("2. Add Food Item")
    print("3. Update Food Item")
    print("4. Delete Food Item")
    print("5. Add Customer")
    print("6. Place Order")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        add_food()

    elif choice == "3":
        update_food()

    elif choice == "4":
        delete_food()

    elif choice == "5":
        add_customer()

    elif choice == "6":
        place_order()

    elif choice == "7":
        print("\nThank You for using Restaurant Management System!")
        break

    else:
        print("\n❌ Invalid Choice! Please try again.")