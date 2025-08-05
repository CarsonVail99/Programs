import random

def computer_roll():
    return random.randint(1,12)

def player_roll():
    while True:
        roll = str(input("Enter x to roll dice:"))
        if roll == "x":
            return random.randint(1,12)

def game():
    player_score = 0
    computer_score = 0
    while player_score < 3 and computer_score < 3:
        comp_roll = computer_roll()
        play_roll = player_roll()
        if comp_roll > play_roll:
            computer_score += 1
            print(f'player rolled: {play_roll}, computer rolled: {comp_roll} \n'
                  f'Computer won!\nPlayer score is:', player_score, f'Computer score is:', computer_score)
        elif play_roll > comp_roll:
            player_score += 1
            print(f'player rolled: {play_roll}, computer rolled: {comp_roll} \n'
            f'Player won!\nPlayer score is:', player_score, f'Computer score is:', computer_score)
        elif play_roll == comp_roll:
            print(f'Both you and computer rolled same number, Reroll')
        else:
            print("Invalid input")
    if player_score == 3:
        print(f'Player won!\nPlayer score is:', player_score, f'Computer score is:', computer_score)
        return False
    else:
        print(f'Computer won!\nPlayer score is:', player_score, f'Computer score is:', computer_score)
        return False
def main():
    def menu():
        while True:
            print("Welcome to dice rolling game!")
            q = input("Press x to start game\nPress q to quit")
            if q == 'x':
                game()
            elif q == 'q':
                return False
            else:
                print("Invalid input\nPress x to roll dice\nPress q to quit")
    menu()

if __name__ == "__main__":
    main()
