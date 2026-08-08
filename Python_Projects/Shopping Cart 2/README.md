# Shopping Cart Application

A console-based Python application built to practice lists, dictionaries, and application control flow by creating an interactive store billing system.

## Features

* **Add Products:** Displays store inventory and adds items dynamically into a personal shopping cart as dictionaries inside a list.
* **Remove Products:** Finds the item's position in the cart list and removes it using `pop()`.
* **Calculate Bill:** Totals up prices of all items in the cart on demand by looping through the cart list.
* **Check Cart:** Displays a real-time list of all selected products currently inside the cart.

## Visual Examples

1. View Inventory and Add Item

```
Available Products with price :  {'Monitor': 300, 'Mouse': 100, 'Keyboard': 150, 'TV': 500, 'Bag': 250, 'Pen': 60, 'Pencil': 20}
Type the item to add : Monitor
Monitor added successfully !
```

2. Check Cart

```
Your Cart : 
Monitor  -  300
```

3. Calculate and Display Bill

```
The total bill is  300
```

## How to Run

1. Make sure you have Python installed on your system.
2. Save the script as `cart.py`.
3. Open your terminal and run:

```
python cart.py
```

4. Choose an option from the menu (1–5) and input item names exactly as listed in the inventory.