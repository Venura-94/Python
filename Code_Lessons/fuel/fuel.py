menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order = {}
    total_cost = 0

    print("Welcome to Felipe's Taqueria! Place your order:")

    while True:
        try:
            item = input().title()
        except EOFError:
            break

        price = menu.get(item)
        if price is not None:
            order[item] = price
            total_cost += price
        else:
            print("Item not found on the menu. Please choose a valid item.")

        print(f"Total cost: ${total_cost:.2f}\n")

    print("Thank you for your order!")

if __name__ == "__main__":
    main()