import itertools
from collections import defaultdict

class InventoryManagement:
    def __init__(self):
        # Initialize inventory with items and quantities
        self.inventory = {
            'apple': 50,
            
            'banana': 30,
            'orange': 40,
            'grape': 20
        }
        # Set stock threshold for replenishment alerts
        self.stock_threshold = 10
        # Sales log to track sales history
        self.sales_log = defaultdict(list)

    def display_inventory(self):
        """Display current inventory levels."""
        print("\nCurrent Inventory Levels:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity} units")
        print()

    def record_sale(self, item, quantity):
        """Record the sale of an item and update inventory."""
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            self.sales_log[item].append(quantity)
            print(f"Sale recorded: {quantity} {item}(s) sold.\n")
            self.check_replenishment(item)
        else:
            print(f"Error: Not enough {item} in stock or item doesn't exist.\n")

    def check_replenishment(self, item):
        """Check if any item needs replenishment based on stock level."""
        if self.inventory[item] < self.stock_threshold:
            print(f"ALERT: {item} stock is low ({self.inventory[item]} units left). Consider replenishing.\n")

    def replenish_stock(self, item, quantity):
        """Replenish the stock for a given item."""
        if item in self.inventory:
            self.inventory[item] += quantity
            print(f"Replenished {item} with {quantity} units.\n")
        else:
            print(f"Error: {item} does not exist in the inventory.\n")

    def view_sales_log(self):
        """View sales history grouped by item."""
        print("\nSales History:")
        grouped_sales = dict(itertools.groupby(sorted(self.sales_log.items()), key=lambda x: x[0]))
        for item, sales in grouped_sales.items():
            sales_quantities = list(itertools.chain(*[s[1] for s in sales]))
            print(f"{item}: Sold {sum(sales_quantities)} units in total.")
        print()

# Create an instance of the InventoryManagement system
inventory_system = InventoryManagement()

# Interact with the system
def interact_with_inventory():
    while True:
        print("Choose an action:")
        print("1. Display Inventory")
        print("2. Record Sale")
        print("3. Replenish Stock")
        print("4. View Sales Log")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            inventory_system.display_inventory()

        elif choice == '2':
            item = input("Enter the item sold: ").lower()
            quantity = int(input(f"Enter the quantity of {item} sold: "))
            inventory_system.record_sale(item, quantity)

        elif choice == '3':
            item = input("Enter the item to replenish: ").lower()
            quantity = int(input(f"Enter the quantity of {item} to add: "))
            inventory_system.replenish_stock(item, quantity)

        elif choice == '4':
            inventory_system.view_sales_log()

        elif choice == '5':
            print("Exiting Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

# Start the interactive session
interact_with_inventory()