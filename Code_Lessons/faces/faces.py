def replace_emoticon(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    input_text = input()
    replaced_text = replace_emoticon(input_text)
    print(replaced_text)

main()
