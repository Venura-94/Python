def main() :

    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

    input_strings = input("Input : ")

    result_string = ""

    for char in input_strings:
        if char not in vowels:
            result_string += char
            print(f"Output: {result_string}")

if __name__ == "__main__":
    main()