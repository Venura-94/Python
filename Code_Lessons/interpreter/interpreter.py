def main():

    expression = input("Expression:")
    x, y, z = expression.split(" ")

    x = int(x)
    z = int(z)

    result = calculator_expression(x, y, z)
    formatted_result = format(result, ".1f")
    print(formatted_result)


def calculator_expression(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "/":
        return x / z
    elif y == "*":
        return x * z

main()


