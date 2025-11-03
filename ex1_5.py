#Exercise 1.5: Shopping Cart System

# Problem Description:
# Build a shopping cart system with the following features:


# 1. Add items (name, price, quantity)
# 2. Remove items
# 3. Update quantity
# 4. Calculate total price
# 5. Apply discount code (10% off if total > $100)
# 6. Display cart summary


# Expected Output:
# Shopping Cart Menu:

# Choice: 1

# Product { 'apple' : { price : 1.2, quantity : 5} }
products = { 'apple' : { 'price' : 1.2, 'quantity' : 5} }

def shopping_cart_system():
    while True:
        PrintMenu('Shopping Cart System', ['Add item', 'Remove item', 'Update quantity', 'View cart', 'Checkout', 'Exit'])
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            add_items(name, price, quantity)
        elif choice == '2':
            name = input("Enter item name to remove: ")
            remove_items(name)
        elif choice == '3':
            name = input("Enter item name to update quantity: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(name, quantity)
        elif choice == '4':
           display_cart_summary()
        elif choice == '5':
            print(f'Total Price: {apply_discount_code(calculate_total_price())}')
        elif choice == '6':
            print("Exiting Shopping Cart System.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

def add_items(name, price, quantity):
    name = name.lower()
    if name in products.keys():
        products[name]['quantity'] += quantity
    else:
        products[name] = {'price': price, 'quantity': quantity}
    if products[name]['price'] != price:
        if input(f"U want update price of {name} ?(y/n)").lower() == 'y':
            products[name]['price'] = price

def remove_items(name):
    if name in products.keys():
        products.pop(name.lower())
        print(f'Done remove {name}')
    else:
        print(f'Done remove {name} not\'t fond')

def update_quantity(name, quantity):
    if name in products.keys():
        products[name]['quantity'] += quantity

def calculate_total_price():
    total_price = 0
    for n in products.keys():
        total_price += products[n]['price']
    return total_price

def apply_discount_code(total):
    if total > 100 :
        return (total - (total * 0.1))
    else :
        return total
    
def display_cart_summary():
    for n in products.keys():
        print(f'👉 {n}\n\t 💰 Price: {products[n]['price']}\n\t 🛒 Quantity: {products[n]['quantity']}\n\t 💲 Total Price: {products[n]['quantity'] * products[n]['price']}')

def PrintMenu(name: str ,options: list[str]):
    name = name if len(name) % 2 == 0 else name + ' '
    print('╔' + '═'*50 + '╗')
    print('╟'+ ('─'* (25 - int(len(name)/2))) + name +('─'* (25 - int(len(name)/2)))+'╢')
    print('╠═══╦' + '═'*46 + '╣')
    for i in range(0, len(options)):
        print(f'║ {i+1} ║'+(' ' + options[i]+ ' '*60)[:46]+ '║')
        if(i < len(options)-1): print('╠═══╬' + '═'*46 + '╣')
    print('╚═══╩' + '═'*46 + '╝')
    
shopping_cart_system()