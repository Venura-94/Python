import inflect

def bid_adieu(names):
    p = inflect.engine()
    n = len(names)

    if n == 1:
        return f'Adieu, adieu, to {names[0]}'

    farewell = f'Adieu, adieu, to {", ".join(names[:-1])}'
    if n == 2:
        farewell += f' and {names[-1]}'
    else:
        farewell += f', and {names[-1]}'

    return farewell

if __name__ == "__main__":
    names = []
    print("Enter names, one per line. Press Ctrl-D (Ctrl-Z on Windows) to finish.")

    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    farewell_message = bid_adieu(names)
    print(farewell_message)
