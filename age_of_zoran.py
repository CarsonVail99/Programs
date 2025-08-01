import random
import time

class Player:

    def __init__(self, name, phy_damage, attack, defence, magic_damage, magic_defence):
        self.name = name
        self.phy_damage = phy_damage
        self.health = 10
        self.attack =  attack
        self.defence = defence
        self.magic_damage = magic_damage
        self.magic_defence = magic_defence
        self.experience = 0
        self.lvl = self.experience /100

    @property
    def level(self):
        return self.experience/100

    @classmethod
    def create_warrior(cls):
       return cls('Warrior',10, 0.75, 0.25, 1, .05)

    @classmethod
    def create_paladin(cls):
        return cls('Paladin', 4, 0.75, 0.20, 6, .15)

    @classmethod
    def create_mage(cls):
        return cls ('Mage', 1, 0.80, 0.05, 12, .25)

    @classmethod
    def create_hunter(cls):
        return cls('Hunter', 6, 0.80, 0.15, 5, .20)

    @classmethod
    def create_god(cls):
        return cls('slave4', 10, 0.99, 0.99, 10, .99)


class Monster:

    def __init__(self, name, phy_damage, attack, defence, magic_damage, magic_defence):
        self.name = name
        self.phy_damage = phy_damage
        self.health = 10
        self.attack = attack
        self.defence = defence
        self.magic_damage = magic_damage
        self.magic_defence = magic_defence


    @classmethod
    def create_monster(cls):
        monster_types = [
            ('Goblin', 1, 0.50, 0.25, 3, .10),
            ('Orc', 2, 0.50, 0.25, 4, .10),
            ('Troll', 4, 0.50, 0.25, 4, .25),
            ('Dragon',4, 0.5, 0.20,5,.25)]
        monster = random.choice(monster_types)
        return cls(*monster)


def handle_physical_attack(attacker, defender):
    while defender.health > 0:
        if random.random() > defender.defence:
            damage = int(attacker.phy_damage) - (defender.defence * 4)
            defender.health -= damage
            print(f'{attacker.name} hit the {defender.name} for {damage} physical damage!')
            return
        else:
            print(f'{attacker.name} missed!')
            return


def handle_magic_attack(attacker, defender):

   while defender.health > 0:
        if random.random() > defender.magic_defence:
            damage = attacker.magic_damage - defender.magic_defence
            defender.health -= damage
            print(f'{attacker.name} hit the {defender.name} for {damage} magic damage!')
            return
        else:
            print(f'{attacker.name} missed the {defender.name}!')
            return


def handle_defend(player):
    player.defence = 1.15*player.defence
    print(f'{player.name} takes a defensive stance!')


# def encounter(player, monster):
#     time.sleep(1)
#     first_attacker = random.choice([player, monster])
#     if first_attacker == player:
#         time.sleep(1)
#         print(f'{player.name} gets to attack first!')
#     else:
#         time.sleep(1)
#         print(f'the {monster.name} strikes first!')
#         # Players turn

def combat(player, monster):
    first_attacker = random.choice([player, monster])
    combat_counter = 0
    combat_counter += 1
    if first_attacker == player:
        while True:
            player_turn(player, monster)
            monster_turn(monster, player)
            if monster.health <= 0:
                print(f'You have killed the {monster.name}!\n'
                    f'You gained {player.experience + 50} total EXP and are level {player.level + 0}')
                return False

            if player.health <= 0:
                print(
                    f'You have ascended from this plane of existence and are in a undescribale place that cant be writen!')
                print(f'You gained {player.experience} total EXP and are level {player.level + 0}')
                return False
            else:
                while True:
                    monster_turn(monster, player)
                    player_turn(player, monster)
                    if monster.health <= 0:
                        player.experience += 50
                        print(f'You have killed the {monster.name}!\n'
                        f'You gained {player.experience + 50} total EXP and are level {player.level + 0}')
                        return False

                    elif player.health <= 0:
                        print(f'You have ascended from this plane of existence and are in a undescribable place that cant be writen!')
                        print(f'You gained {player.experience} total EXP and are level {player.level + 0}')
                        return False
    return player


def display_status(player, monster):
    print('\n' + "-"*40)
    time.sleep(.5)
    print(f"Your health: {player.health:1f} | {monster.name}'s health: {monster.health:1f}")
    time.sleep(.5)
    print('\n' + "-" * 40)


def player_turn(player, monster):
    display_status(player, monster)
    print('\nEnter your action')
    print('1. Physical Attack')
    print('2. Magic Attack')
    print('3. Defend (+20% defence)')
    try:
        choice = int(input('Enter your choice (1-3): '))
        if choice == 1:
            handle_physical_attack(player, monster)

        elif choice == 2:
            handle_magic_attack(player, monster)

        elif choice == 3:
            handle_defend(player)
        else:
            print('Invalid choice, please try again')
    except Exception as e:
        print(e)


def monster_turn(monster, player):
    #monster randomly chooses between physical and magic attack
    attack_type = random.choice(['physical', 'magic'])
    if attack_type == 'physical':
        print(f'{monster.name} attempts a physical attack!')
        return handle_physical_attack(monster, player)
    else:
        print(f'{monster.name} casts a spell on you!')
        return handle_magic_attack(monster, player)


def main_menu(player=None):
    print (80*'-', '\nWelcome to Age of Zoran', 56*'-')
    print(80*'-')
    time.sleep(2)
    print('loading...')
    time.sleep(2)
    print('Zoran is a 100 year old man, he is a warrior, he is a paladin, he is a mage and he is a hunter')
    time.sleep(.25)
    print('\n\nChoose your class')
    time.sleep(.5)
    print('1. Warrior - Cool guy, woke up like this, and hes got a lot of strength')
    time.sleep(.35)
    print('2. Paladin - Hes an average religous type of guy, good values, but hes not that cool')
    time.sleep(.30)
    print('3. Mage - He knows all there is to know in this universe and beyond, we dont know where you learn this shit from')
    time.sleep(.25)
    print('4. Hunter - This guy is a coin type of guy, he has been around for quite some time, a dog can learn tricks?')
    time.sleep(.15)
    while True:
        try:
            choice = int(input('Enter the class you want to play as in Zoran:'))
            if 1 <= choice <= 5:
                break
            print('Invalid choice, please try again')
        except ValueError:
            print('Please enter a number 1-4')

    if choice == 1:
        player = Player.create_warrior()

    elif choice == 2:
        player = Player.create_paladin()

    elif choice == 3:
        player = Player.create_mage()

    elif choice == 4:
        player = Player.create_hunter()

    else:
        player = Player.create_god()

    print(f'You have chosen {player.name} as your class and are ready to fight!')
    game_loop(player)

def loading_level(player):
    levels = 0
    levels += 1
    print(levels)
    stages1 = (
        'Loopy', 'Valley', 'Windy', 'Frozen', 'Rocky', 'Slimy', 'Dark',
        'Depressing', 'Scary', 'bright', 'Mystery',
        'Sunny', 'Milky', 'Vast', 'Unlimited', 'Marshy', 'Moonlit')
    random_stage = random.choice(stages1)
    stages2 = (
        'space', 'hills', 'shrine', 'Mountains', 'Supermarket', 'lando', 'zoo', 'Hell', 'Cage', 'Mentality', 'Airport', 'Waters',
        'Road', 'Room', 'Reality', 'dimension')
    random_stage2 = random.choice(stages2)
    stage3 = f'{random_stage} {random_stage2}'
    message = f'The past horrors of {stage3} makes the {player.name} wish he/she had never came back'
    print(message)
    current_monster = Monster.create_monster()

def battle_overview(player):
    level_up(player)
    question = input('Would you like to 1.continue? or 2.leave?')
    if question == '1':
        print(f'Ok carry on young {player.name}!')
        return
    elif question == '2':
        print(f'Too bad, you fight until you die!')
        return
    else:
        print('Invalid choice, please try again')


def level_up(player):
    print(f'You are now level {player.level}!')
    if player.lvl > 0:
        print(f'You have leveled up to level {player.level}!')
        player.health = 3 + 1.05 * player.level
        lvl_up_skill = input('Which skill would you like to level up? (1.phy, 2.magic, 3.def, 4.magic_def)')
        if lvl_up_skill == 1:
            player.phy_damage = 1 + 1.05 * player.level

        elif lvl_up_skill == 2:
            player.magic_damage = 1 + 1.05 * player.level
        elif lvl_up_skill == 3:
            player.defence = 1.05 * player.defence
        else:
            player.magic_defence = 1.05 * player.magic_defence
    else:
        print(f'You didnt level up, but are level {player.level}!')

def game_loop(player):
    while True:
        current_monster = Monster.create_monster()
        print(f'A Random {current_monster.name} has appeared from the darkness')
        while player.health > 0:
            loading_level(player)
            combat(player, current_monster)

def handle_victory(player,current_monster):
    print(f'You killed {current_monster.name}!')
    print(f'You gained {player.experience + 50} total EXP and are level {player.level + 0}')
    return False

def handle_death(player, current_monster):
    print(f'{current_monster.name} has killed you!')
    print(f'You gained {player.experience} total EXP and are level {player.level + 0}')
    return False





if __name__ == '__main__':
    main_menu()













    # while True:
    #     current_monster = Monster.create_monster()
    #     combat()
    #     while current_monster.health > 0 and player.health > 0:
    #
    #         if player_turn(player, current_monster):
    #             if current_monster.health <= 0:
    #                 gained_exp = random.randint(34, 60) * player_level
    #                 player.experience += gained_exp
    #                 print(f'You gained {gained_exp}!')
    #                 if player.experience >= exp_to_next_level:
    #                     player_level += 1
    #                     exp_to_next_level += 100*player_level*1.15
    #                     print(f'You have leveled up to level {player_level}!')
    #                     time.sleep(1)
    #                     player.health = 100+1.5*player_level
    #                     player.phy_damage = 1+1.5*player_level
    #                     player.magic_damage = 1+1.5*player_level
    #     else:
    #         if current_monster.health > 0:
    #             print(f'{current_monster.name} turn')
    #             if monster_turn(current_monster, player):
    #                 if player.health <= 0:
    #                     print('You have died!', 80*'=')
    #                     return player_turn
    #
    #
    #     print(f'\n Current status:)')
    #     print(f'Level: {player.level} | EXP: {player.experience}/'+f'{exp_to_next_level}')
    #     print(f'Health: {player.health}/100')
    #     while True:
    #         choice = input('\nWould you like to continue? \n1. Continue to next stage\n2. Rest(Heals You!)\n3. Exit\n Choose 1, 2 or 3: ')
    #         if choice == '1':
    #             return game_loop(player)
    #         elif choice == '2':
    #             player.health = min(player.health + 20 + player_level) * 1.5
    #         else:
    #             print('Thanks for playing!')
    #             return True


# if __name__ == '__main__':
#     main_menu()















    #
    # print('loading level one')
    # time.sleep(1)
    # while True:
    #     combat(player, Monster.create_monster())
    #     if player.health >= 0:
    #         return game_loop(player)
    #     else:
    #         print('YOU ARE DEAD!')
    #     print(f'You won battle(s) and are now level {player.level + 0}!')
    #     inputs = input('Would you like to continue? (y/n)')
    #     if inputs == 'y':
    #         return game_loop(player)
    #     else:
    #         print('Thanks for playing!')









#
# attacksequence
# display_status(player, monster)
# 
# if attacksequence % 2 != 0:
#     monster_turn(monster, player):
# else:
#     player_turn(player, monster):

# def main(player,menu):
#     menu(input('What class would you like to play? Enter the class you want to play as Warrior, Paladin, Mage, Hunter:'))
#     if menu == "Warrior":
#         print('You have chosen Warrior')
#         player = Player('Warrior', 10, 0.65, 0.70, 2, .60)
#     elif menu == 'Paladin':
#         print('You have chosen Paladin')
#         player = Player('Paladin', 4, 0.75, 0.70, 6, .65)
#     elif menu == 'Mage':
#         print('You have chosen Mage')
#         player = Player('Mage', 1, 0.80, 0.35, 12, .80)
#     elif menu == 'Hunter':
#         print('You have chosen Hunter')
#         player = Player('Hunter', 7, 0.50, 0.55, 6, .55)
#     elif menu == 'slave4':
#         hunter = Player('...', 10, 10, 10, 10, 10)
#     else:
#         print('That is not a valid class.')
#         return
#
#
#
#
#     def first_encounter():
#         random_monster = random.randint(0,3)
#         if random_monster == 0:
#             monster = Monster('Braindead Monster', 1, 0.35, 0.25, 3, .75)
#             print(f'A {monster.name} has appeared!')
#         elif random_monster == 1:
#             monster = Monster('Braindead Monster', 2, 0.50, 0.65, 4, .35)
#             print(f'A {monster.name} has appeared!')
#         else:
#             monster = Monster('Braindead Monster', 10, 0.50, 0.65, 10, .65)
#             print(f'A {monster.name} has appeared!')
#         return random_monster





    #     if monster.health <= 0:
    #          print(f'You've killed the {monster.name}!')
    # else:
    #      monster_turn(monster, player)
    #      if player.health <= 0:
    #          print(input('You have died'))
    #          break
#     print(f'Your health is {player.health}/100\nThe opponents health is {monster.health}/100')
#
# def player_turn(player, monster, choice):
#     choice=input(('what type of attack would you like to use?\n 1:physical\n 2:magic'))
#     if choice == 1:
#         damage = (random.randint(0,1)(player.phy_damage) - (monster.defence*2))
#         print("you've chosen physical attack!")
#     return monster.health - damage
#
#     else:
#         magic_damage = (random.randint(0,1)(player.magic_damage)) - monster.magic_defense*2)
#         print("You've chosen magic attack")
#     return monster.health - magic_damage
#     def hit_or_miss = random.randint(0,1)
#         if hit_or_miss == 0:
#             print(f'You hit the monster with {player.phy_damage or magic_damage} damage! The monster has {monster.health} health left')
#         else:
#             print('You missed!')
#             return monster.health - player.phy_damage




        







