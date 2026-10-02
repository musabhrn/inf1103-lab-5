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

def save_inventory(inventory):
    print("Saving inventory...")
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)
    print(f"Inventory saved successfully to {FILENAME}.\n")

def add_product(inventory):
    print("Add new product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)
    print("\nProduct added successfully!\n")


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

        if option == "2":
            add_product(inventory)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()