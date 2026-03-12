# ---------------------------------------------------
# Bookstore Inventory Management & Data Analysis
# ---------------------------------------------------

# -----------------------------
# Task 1: Inventory Restocking Analysis
# -----------------------------

inventory = {
    "Python Basics": 15,
    "Data Science": 8,
    "Web Development": 12,
    "Machine Learning": 5,
    "Database Design": 3,
    "Cloud Computing": 18
}

reorder_list = {}   # Dictionary to store books needing reorder

print("----- Inventory Restocking Analysis -----")

# Loop through dictionary using items()
for book, stock in inventory.items():

    # Check if stock is less than 10
    if stock < 10:
        quantity_needed = 10 - stock
        print(f"Reorder {book}: Need {quantity_needed} more books")

        # Add to reorder list dictionary
        reorder_list[book] = quantity_needed

    else:
        print(f"{book}: Stock sufficient")

print("\nBooks needing reorder:", reorder_list)


# -----------------------------
# Task 2: Nested Conditional Logic for Pricing
# -----------------------------

prices = {
    "Python Basics": 450,
    "Data Science": 850,
    "Web Development": 550,
    "Machine Learning": 950,
    "Database Design": 650,
    "Cloud Computing": 750
}

print("\n----- Book Price & Stock Category -----")

for book, stock in inventory.items():

    price = prices[book]

    # First condition: check stock
    if stock < 10:

        # Nested condition: check price
        if price > 700:
            print(f"{book}: High-value restock needed")
        else:
            print(f"{book}: Standard restock needed")

    else:

        # Nested condition for stock OK
        if price > 700:
            print(f"{book}: Premium item, stock OK")
        else:
            print(f"{book}: Standard item, stock OK")


# -----------------------------
# Task 3: Dictionary Data Cleaning
# -----------------------------

new_inventory = {
    "AI Fundamentals": 12,
    "Cybersecurity": None,
    "Blockchain": 8,
    "IoT Basics": None,
    "DevOps": 15
}

print("\n----- Cleaned Inventory -----")

for book, stock in new_inventory.items():

    # Check for missing value
    if stock is None:
        new_inventory[book] = 0

    print(f"{book}: {new_inventory[book]}")