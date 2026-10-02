import json
import os

FILENAME = "inventory.json"

def load_inventory():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            print(f"{FILENAME} found.")
            print("Inventory loaded successfully.\n")
            return json.load(file)
    else:
        print(f"{FILENAME} not found. Starting with empty inventory.\n")
        return []

def display_menu():
    print("=" * 35)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 35)
    print()

def main():
    display_menu()
    inventory = load_inventory()

    while True:
        print("--------MENU--------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("--------------------\n")

        option = input("Enter option: ").strip()
        print()

        if option == "6":
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()