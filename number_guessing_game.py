import random

def number_guessing_game():
    guess_counter = 0
    computer_number = random.randint(1,10)
    while guess_counter < 3:
        guess_number = int(input('Guess a number between 1 and 10: '))
        if guess_number == computer_number:
            print(f'You guessed the number in {guess_counter} tries!')
            break
    
        elif guess_number > computer_number:
            print('Too high!')
            guess_counter += 1
        elif guess_number < computer_number:
            print('Too low!')
            guess_counter += 1
    print(f'Game Over! {computer_number} was the number')


def main():
    try:
        number_guessing_game()
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()



