# Initialize an empty list to store the customer's order
order =[]

# Printing the menu
menu_items ={ 
    1: {"name": "Apple", "price": 0.49},
    2: {"name": "Tea-Thai iced", "price": 3.99},
    3: {"name": "Fried banana", "price": 4.49}
}

order = []

# Display menu
def display_menu():
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['name']} - ${value['price']:.2f}")


# Get the customer's order
def get_order():
    while True:
        display_menu()
        menu_selection = input("Please enter the number of the items you'd like to order:")

        if not menu_selection.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        menu_selection = int(menu_selection)
        if menu_selection not in menu_items:
            print("Invalid selection. Please choose a valid menu item number.")
            continue

        item_name = menu_items[menu_selection]["name"]
        price = menu_items[menu_selection]["price"]

        quntity = input(f"How many{items_name}s would you like to order? (Default is 1): ")
        if not quantity.isdigit():
            print("Invalid input. Quantity set to 1.")
            quantity = 1
        else:
            quantity = int(quantity)

        order.append({
            "Item name": item_name,
            "Price": price,
            "Quantity": quantity
        })    
        while True:
            continue_ordering = input("Would you like to ordcer something else? (y/n):").lower()
            if continue_ordering == 'y':
                break
            elif continue_ordering == 'n':
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# Print the receipt
def print_receipt():
    print("\nReceipt:")
    print("Item name          | Price   |Quantity")
    print("-------------------|---------|---------")         

    for item in order:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        name_space = ''*(26 - len(item_name))
        price_space = ''*(6 - len(f"{price:.2f}"))

        print(f"{item_name}{name_space}| ${price.2f}{price_space}| {quantity}")

total = sum(item["Price"] * item["Quantity"] for item in order)
print("\nTotal price: ${:.2f}".format(total))

# Run the Order
def main():
    get_order()
    print("Thank you for your order.")
    print_receipt()

if __name__=="__main__":
    main()
        



 Source Title 1:   https://www.google.com/
 Source Title 2:   https://openai.com/chatgpt/
