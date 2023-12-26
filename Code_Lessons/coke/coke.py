def main():
    accepted_denominations = [25, 10, 5]
    amount_due = 50
    print(f"Amount Due: {amount_due}")
    n=0
    while amount_due > 0:
        n=int(input("Insert Coin :"))
        if n in accepted_denominations:
            amount_due =amount_due-n
            if amount_due > 0:
                print(f"Amount Due : {amount_due}")

            if amount_due < 0:
                change = abs(amount_due)
                print(f"Change Owed: {change}")
        else:
            print ("Amount Due : 50")

if __name__== "__main__":
    main()