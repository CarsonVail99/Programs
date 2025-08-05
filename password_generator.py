import random
import string


def length_generate():
    try:
        length = int(input('Enter password length:'))
        if length < 8:
            print('Password length should be greater than 8')
            return length_generate()
        elif length > 16:
            print('Password length should be less than 16')
            return length_generate()
        else:
            return length
    except ValueError as e:
        print(e)


def pw_generate(length):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation
    all_char = letters + digits + special_char
    password = ''.join(random.choice(all_char) for i in range(length))
    print(f'Your password is: {password}')


def main():
    pw_generate(length_generate())


if __name__ == "__main__":
    main()

