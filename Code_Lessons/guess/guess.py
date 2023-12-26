import random

def get_level():
    while True:
        try:
            user_input = int(input("level:"))
            if user_input >0:
                return user_input
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            user_guess = int(input("guess:"))
            if user_guess >0:
                return user_guess
        except ValueError:
            pass


def main():
    level = get_level()
    secret_number = random.randint(1, level)

    while True:
        guess = get_guess()
        if guess < secret_number:
            print("too small")
        elif guess > secret_number:
            print("too large")
        else:
            print("just right")
            break

if __name__=="__main__":
    main()
