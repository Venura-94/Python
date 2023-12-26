def get_media_type(filename):
    lowercase_filename = filename.lower()

    if lowercase_filename.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf")):
        return f"image/{lowercase_filename.split('.')[-1]}"
    elif lowercase_filename.endswith((".txt", ".zip")):
        return f"document/{lowercase_filename.split('.')[-1]}"
    else:
        return "application/octet-stream"

def main():
    x = input("File name: ").strip()
    media_type = get_media_type(x)
    print(media_type)

if __name__ == "__main__":

    main()
