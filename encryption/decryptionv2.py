import random
import string


def encryption(chars, shuffled_chars):
    plain_message = input('Enter your message:')
    encrypted_message = ''
    for letter in plain_message:
        encrypted_location = chars.index(letter)
        encrypted_message += (shuffled_chars[encrypted_location])
    print(f'Your encrypted message is: {encrypted_message}')
    return encrypted_message

def decryption(encrypted_message,shuffled_chars, chars):
    decrypted_message = ''
    for letter in encrypted_message:
        decrypted_location = shuffled_chars.index(letter)
        decrypted_message += (chars[decrypted_location])
    print(f'Your decrypted message is: {decrypted_message}')

def main(encrypted_message = None):
    chars = list(string.ascii_letters + string.digits + string.punctuation)
    shuffled_chars = chars.copy()
    random.shuffle(shuffled_chars)

    while True:
        action = input('Press\n1.Encrypt:\n2.Decrypt:\n3.Exit:\n')
        if action == '1':
            encrypted_message = encryption(chars, shuffled_chars)
        elif action == '2':
            decryption(encrypted_message, shuffled_chars, chars)
            if encrypted_message is None:
                print('You need to encrypt your message first')
                continue
        elif action == '3':
            break
        else:
            print('Invalid choice, please try again')


if __name__ == '__main__':
    main()




