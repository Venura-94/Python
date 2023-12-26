def main():

    order = {}

    while True:
            try:
                item = input().strip().lower()
                if not item:
                    continue
                if item in order:
                 order[item] += 1
                else:
                 order[item] = 1
            except EOFError:
                break

    first_item = True  # Flag to track the first item

    for key, value in order.items():
        if first_item:
            print(f"\n{key.upper()}: {value}")
            first_item = False
        else:
            print(f"{key.upper()}: {value}")


if __name__ == "__main__":
    main()
