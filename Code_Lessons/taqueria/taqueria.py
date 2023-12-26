d = {
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

    while True:
        try:
            item = input("Item:").title()
        except EOFError:
            break

        price = d.get(item)
        if price is not None:
            order[item] = price
            total_cost += price
        else:
            print("Item not in the shop")

        print(f"Total Cost: ${total_cost:.2f}")
if __name__ == "__main__":
    main()