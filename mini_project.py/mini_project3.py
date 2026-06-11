'''Priya's Cafe System
1. order: 'mocha','tea','Green tea','cold coffee', 'Latte', 'Cappuccino', 'Espresso',
2. size: 'small-240', 'medium-320', 'large-360'
3. price: 'mocha'- 150, 'tea'- 100, 'Green tea'- 120, 'cold coffee'- 130, 'Latte'- 140, 'Cappuccino'- 160, 'Espresso'- 170
4. quantity: input from user
5. add-on: biscuit, cookies
6. Total Discount: 15% if total price is above 700
7. total price: price * quantity
'''


MENU = {
    "mocha": 150,
    "tea": 100,
    "green tea": 120,
    "cold coffee": 130,
    "latte": 140,
    "cappuccino": 160,
    "espresso": 170
}

SIZE_EXTRA = {
    "small": 240,
    "medium": 320,
    "large": 360
}

ADDONS = {
    "biscuit": 20,
    "cookies": 30
}


def display_menu():
    print("\n===== PRIYA'S CAFFE MENU =====")

    for item, price in MENU.items():
        print(f"{item.title()} - ₹{price}")

    print("\nSizes:")
    for size, extra in SIZE_EXTRA.items():
        print(f"{size.title()} (+₹{extra})")

    print("\nAdd-ons:")
    for addon, price in ADDONS.items():
        print(f"{addon.title()} - ₹{price}")


def calculate_bill():
    order_id = input("\nEnter Order ID: ")

    drink = input("\nEnter drink: ")

    if drink not in MENU:
        print("Invalid drink selected.")
        return

    size = input("Enter size (small/medium/large): ")

    if size not in SIZE_EXTRA:
        print("Invalid size.")
        return

    quantity = int(input("Enter quantity: "))

    addon = input(
        "Add-on (biscuit/cookies/none): "
    ).lower()

    addon_price = 0

    if addon != "none":
        if addon not in ADDONS:
            print("Invalid add-on.")
            return
        addon_price = ADDONS[addon]

    item_price = MENU[drink] + SIZE_EXTRA[size]

    subtotal = (item_price + addon_price) * quantity

    discount = 0

    if subtotal > 700:
        discount = subtotal * 0.15

    final_amount = subtotal - discount

    print("\n========== BILL ==========")
    print(f"Order ID : {order_id}")
    print(f"Drink    : {drink.title()}")
    print(f"Size     : {size.title()}")
    print(f"Quantity : {quantity}")
    print(f"Addon    : {addon.title()}")
    print(f"Subtotal : ₹{subtotal:.2f}")
    print(f"Discount : ₹{discount:.2f}")
    print(f"Total    : ₹{final_amount:.2f}")
    print("==========================")
    

display_menu()
calculate_bill()
