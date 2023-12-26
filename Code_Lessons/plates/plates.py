def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def has_letters_at_start(s):
    # Check if the first two characters are letters
    return s[0:2].isalpha()

def meets_length_requirements(s):
    # Check if the length is between 2 and 6 characters
    return 2 <= len(s) <= 6

def has_numbers_at_end(s):
    # Check if numbers are only allowed at the end
    return s[:-1].isalpha() and s[-1].isdigit() and s[-1] != '0'

def has_no_special_characters(s):
    # Check if there are no periods, spaces, or punctuation marks
    return all(char.isalnum() for char in s)

def is_valid(s):
    return (has_letters_at_start(s) and
            meets_length_requirements(s) and
            has_numbers_at_end(s) and
            has_no_special_characters(s))

main()