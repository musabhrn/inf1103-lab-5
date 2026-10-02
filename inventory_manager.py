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

if __name__ == "__main__":
    main()