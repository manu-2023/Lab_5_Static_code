"""
Inventory Management System
Provides functionality to add, remove, save, and load inventory items safely.
"""

import json
import logging
from datetime import datetime
import ast

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global inventory data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add quantity of an item to the inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid input types for item or qty: %s, %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove quantity of an item safely."""
    try:
        if item not in stock_data:
            raise KeyError(item)
        if not isinstance(qty, (int, float)):
            raise ValueError("Quantity must be numeric.")

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as err:
        logging.error("Item not found: %s", err)
    except ValueError as err:
        logging.error("Invalid quantity: %s", err)


def get_qty(item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file and return it."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info("Data loaded successfully from %s", file)
            return data
    except FileNotFoundError:
        logging.warning("File not found: %s, creating a new one.", file)
        return {}
    except json.JSONDecodeError as err:
        logging.error("JSON decode error: %s", err)
        return {}


def save_data(file="inventory.json"):
    """Save current inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
            logging.info("Data saved successfully to %s", file)
    except OSError as err:
        logging.error("File operation error: %s", err)


def print_data():
    """Print all items in inventory."""
    logging.info("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the specified quantity threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function for demo operations."""
    data = load_data()

    # Use local variable instead of global
    local_stock = data if data else {}

    # Perform operations on local copy
    local_stock["apple"] = local_stock.get("apple", 0) + 10
    local_stock["banana"] = local_stock.get("banana", 0) + 4
    local_stock["mango"] = local_stock.get("mango", 0) + 3

    if "apple" in local_stock:
        local_stock["apple"] -= 3

    print(f"Apple stock: {local_stock.get('apple', 0)}")
    print(f"Low items: {[i for i, q in local_stock.items() if q < 5]}")

    # Save updates safely
    try:
        with open("inventory.json", "w", encoding="utf-8") as f:
            json.dump(local_stock, f, indent=4)
    except OSError as err:
        logging.error("Error saving data: %s", err)

    print_data()
    ast.literal_eval("{'safe': True}")


if __name__ == "__main__":
    main()
