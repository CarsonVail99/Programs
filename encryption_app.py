import string
import random


class encryption:
    def __init__(self):
        self.characters = string.ascii_letters
        self.digits = string.digits
        self.special_char = string.punctuation
        self.all_char = self.characters + self.digits + self.special_char
        self.encrypted_password = None
        self.encrypted_parts = None


    def encrypt(self):
        password = set(input('Enter your password:'))
        password_length = len(password)
        encrypted_chars = ''.join(random.choice(self.all_char) for i in range(password_length))
        self.encrypted_parts = list(encrypted_chars)
        self.encrypted_password = (password.union(set(self.encrypted_parts)))
        encrypted_password_list = list(self.encrypted_password)
        encrypted_password_list = ''.join(self.encrypted_password)

        print(f'Your encrypted password is: {encrypted_password_list}')
        return self.encrypted_password, self.encrypted_parts


    def decrypt(self,encrypted_password,encrypted_parts):
        if encrypted_password is None or encrypted_parts is None:
            print('You need to encrypt your password first')
            return None
        else:
            decrypted_password = encrypted_password.difference(set(encrypted_parts))
            decrypted_password = list(decrypted_password)
            decrypted_password = ''.join(decrypted_password)
            print(f'Your decrypted password is: {decrypted_password}')
            return decrypted_password


    def menu(self,encrypt,decrypt):
        while True:
            choice = int(input('1. Encrypt Password\n2. Decrypt Password\n3. Exit\n'))
            if choice == 1:
                encrypt()
            elif choice == 2:
                decrypt(self.encrypted_password,self.encrypted_parts)
            elif choice == 3:
                return False
            else:
                print('Invalid choice, please try again')

def main():
    menu = encryption()
    menu.menu(menu.encrypt,menu.decrypt)

if __name__ == '__main__':
    main()


