import emoji

def main():
    user_input = input("Enter a text with emoji codes or aliases: ")
    emojized_text = emoji.emojize(user_input)
    print(emojized_text)

if __name__ == "__main__":
    main()
