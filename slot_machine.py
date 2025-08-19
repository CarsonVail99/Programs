import random
import time

class slot_machine:
    def __init__(self):
        self.slots = 3
        self.reel = 0
        self.bet = 0
        self.balance = 0
        self.member = False
        self.gamble = 0
        self.member_points = 0

    def spin(self):
        if self.bet > 0:
            self.reel = 1

        elif 200 >= self.bet < 300:
            self.reel = 2

        elif self.bet >= 300:
            self.reel = 3

        self.gamble = random.randint(1, 100) * self.reel * self.slots
        return self.gamble


    def winning_sheet(self):

        if self.gamble >= 250 / self.reel:
            self.balance += self.bet * 1.25
            print(f"🍒🍒🍒 You won! 1.25x multiplier! 🍒🍒🍒")
            # 0.1 odds against players
            return self.balance

        elif 310 >= self.gamble > 250 / self.reel:
            self.balance += self.bet * 1.50
            print(f"✨✨✨You won! 1.50x multiplier!✨✨✨")
            return self.balance

        elif 410 >= self.gamble > 310 / self.reel:
            self.balance += self.bet * 1.75
            print(f"🔥🔥🔥 You won! 1.75x multiplier! 🔥🔥🔥")
            return self.balance
        else:
            print(f"❌❌❌ You lost! ❌❌❌")
            self.balance -= self.bet
            return self.balance

    def game(self):
        deposit_counter = 0
        member_ask = int(input('Enter your Binary Casio ID?'))
        self.member_points += member_ask
        if self.member_points >= 4000:
            self.member = True
            print('🥇🥇🥇Welcome back member of the professional gambling squad🥇🥇🥇')
        else:
            print('👎👎👎You are not a member of the professional gambling squad👎👎👎')

        game_selected = input(
                "Welcome to the Binary Casio!\nPress the game you wish to play!\n1.🌟🌟🌟Shooting for the Stars🌟🌟🌟\n2.🐉🐉🐉Lucky Dragon🐉🐉🐉\n3.👽👽👽Flying saucer👽👽👽\n")
        while game_selected == '1' or '2' or '3':
            if self.balance == 0 and deposit_counter == 0:#if new Player
                self.balance = int(input("💰💰💰How much money do you want to play with tonight sir?💰💰💰\n"))
                print(f"You have deposited ${self.balance} into your account.")
                deposit_counter += 1

            while self.balance > 0: #Recurring Player
                print(f'Loading...\nYour balance ${self.balance}')
                if self.balance == 0 and deposit_counter > 0:
                    print('😭😭😭You are out of money😭😭😭')
                    break

                else:#bet
                    self.bet = int(input('💲💲💲How much do you want to bet?💲💲💲'))
                    while self.bet > self.balance: #if bet higher than balance
                        print(f'You dont have enough money to bet ${self.bet}\nBalance: ${self.balance}')
                        self.bet = 0
                        self.bet = int(input('💲💲💲How much do you want to bet?💲💲💲'))
                        print(f'You bet ${self.bet}')
                    if not self.member:
                        if self.member_points >= 4000:
                            self.member = True
                            print('💎💎💎You are now a Diamond Member of the Binary Casio💎💎💎\n💥💥💥Enjoy the free .15 Multiplier of every Bet!💥💥💥')
                            self.bet = self.bet * 1.15

                    if self.bet >= 1:
                        icons = ['✨','🍒','💰','🔥','💎']
                        for x in range(3):
                            slot = [random.choice(icons) for y in range(3)]
                            time.sleep(0.5)
                            print(''.join(slot))

                        self.spin()
                        self.winning_sheet()
                        self.bet = 0 #reset bet
                        self.gamble = 0 #reset self.gamble
                        self.member_points += 50
                    else:
                        print('Please bet at least 1')

        else:#wrong game selected
            print('Please select a valid game')
        return self.balance, self.bet, self.member, deposit_counter


def main():
    while True:
        game = slot_machine()
        game.game()



if __name__ == '__main__':
    main()





