import random

deck = {1: 11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:10, 12:10, 13:10}

def draw_card():
    card_value = random.randint(1,13)
    return deck[card_value]

def calculate_hand_value(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 1:            #ace
            aces += 1
            total += 11
        else:
            total +=deck[card]

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def dealer_play():
    hand = [draw_card(), draw_card()]
    print('Dealer hand is ', hand)
    dealer_value = calculate_hand_value(hand)
    print(f'Dealer has {dealer_value}')

    while dealer_value < 17:
        new_card = draw_card()
        hand.append(new_card)
        dealer_value = calculate_hand_value(hand)
        print(f'dealer draws: {new_card}')
        print(f'dealer has {dealer_value}')

    return dealer_value


def hit_or_stand():
    hand = [draw_card(), draw_card()]
    print('your hand is ', hand)
    player_value = calculate_hand_value(hand)

    while True:
        if player_value >= 21:
            return player_value

        player_action = input("Hit or stand? (h/s)").lower()
        if player_action == "h":
            new_card = draw_card()
            hand.append(new_card)
            player_value = calculate_hand_value(hand)
            print(f'You drew: {new_card}')
        elif player_action == "s":
            return player_value
        else:
            print("Invalid input")


def pre_hand(deposit=0):
    try:
        if deposit == 0:
            deposit = int(input("How much money do you want to deposit?"))
        bet = int(input("How much do you want to bet?"))
        if bet > deposit:
            print("You don't have enough money")
            return deposit, bet
        elif bet <= deposit:
            return deposit, bet
        elif bet <= 0:
            print("You can't bet that")
        return deposit, bet
    except ValueError as e:
        print(e)

def post_hand(deposit,dealer_value,player_value,bet):
    try:
        if player_value > 21:
            print("You busted")
            deposit -= bet
        if dealer_value > 21:
            if player_value <= 21:
                print("Dealer busted")
                deposit += bet
        elif player_value < dealer_value:
            print("Dealer wins")
            deposit -= bet
        elif player_value > dealer_value:
            if player_value <= 21:
                print(f'You win!')
                deposit += bet
        elif player_value == 21:
            print("Blackjack!")
            deposit += bet * 1.5
        elif player_value == dealer_value:
            print("Push")
        return deposit
    except ValueError as e:
        print(e)


def play_again(deposit):
    while deposit > 0:
        print(f'You have {deposit} chips')
        answer = input('You would like to play again?')
        if answer == 'y':
            main(deposit)
        else:
            print('Thanks for playing!')
            print(f'You have {deposit} chips')
            break


def main(deposit=0):
    deposit, bet = pre_hand(deposit)
    player_value = hit_or_stand()
    dealer_value = dealer_play()
    deposit = post_hand(deposit, dealer_value, player_value, bet)
    play_again(deposit)

if __name__ == '__main__':
    main()


