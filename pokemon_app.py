import requests
import random
import time


def get_pokemon_stats(random_pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    print('----------Welcome to the Pokemon Stats App----------')
    decision = input('1. Search for specific Pokemon\n2. Random Pokemon\n3. Exit')
    if decision in ['1']:
        pokemon_caught = input('Enter the pokemon you want to search for:')
        pokemon_info = requests.get(f'{url}{pokemon_caught}').json()
        return pokemon_info
    elif decision in ['2']:
        pokemon_caught = random_pokemon
        pokemon_info = requests.get(f'{url}{pokemon_caught}').json()
        return pokemon_info
    elif decision in ['3']:
        print('Thank you for using our app, Have a great day!')
        return False
    else:
        print('Invalid choice, please try again')


def display_pokemon_info(pokemon_info):
    print(f'Pokemon Name:{pokemon_info["name"]}')
    print(f'Pokemon Weight:{pokemon_info['weight']}')
    print(f'Pokemon Height:{pokemon_info['height']}')
    print(f'Pokemon Base Experience:{pokemon_info['base_experience']}')
    #Pokémon type
    pokemon_type = f'{pokemon_info['types'][0]['type']['name']}'
    pokemon_type = pokemon_type.capitalize()
    print(f'Pokemon type:{pokemon_type}')
    #Pokémon weaknesses
    weakness = weak_against(pokemon_type)
    print(f'Pokemon Weakness:{weakness}')
    #Pokémon abilities
    if len(pokemon_info['abilities']) > 0:
        ability1 = {pokemon_info['abilities'][0]['ability']['name']}
        print(f'Pokemon Ability 1:{ability1}')

        if len(pokemon_info['abilities']) > 1:
            ability2 = {pokemon_info['abilities'][1]['ability']['name']}
            print(f'Pokemon Ability 2:{ability2}')
        else:
            print('Pokemon Ability 2:None')
    else:
        print('Pokemon Ability 1:None\nPokemon Ability 2:None')



def get_pokemon_id():
    poke_dex_url = 'https://pokeapi.co/api/v2/pokemon/?offset=20&limit=1302'
    response = requests.get(poke_dex_url)
    poke_dex_json = response.json()
    i = random.randint(1, 1282)
    random_pokemon = poke_dex_json['results'][i]['name']
    return random_pokemon


def weak_against(pokemon_type):
    weakness = {
    'Bug':'Fire, Flying,  Rock',
    'Dark':'Bug, Fairy, Fighting',
    'Dragon':'Dragon, Fairy, Ice',
    'Electric':'Ground',
    'Fairy':'Poison, Steel',
    'Fighting':'Fairy, Rock, Water',
    'Fire':'Ground, Rock, Water',
    'Flying':'Ice, Rock',
    'Ghost':'Dark, Ghost',
    'Grass':'Poison, Fire, Flying, Ice, Poison',
    'Ground':'Grass, Ice, Water',
    'Ice':'Fire, Fighting, Rock, Steel',
    'Normal':'Fighting',
    'Poison':'Ground, Psychic',
    'Psychic':'Bug, Dark, Ghost',
    'Rock':'Fighting, Grass, Ground, Steel, Water',
    'Steel': 'Fighting, Fire, Ground',
    'Water':'Electric, Grass'
     }
    return weakness[pokemon_type]

def pokemon_app():
        while True:
            pokemon_info = get_pokemon_stats(random_pokemon=get_pokemon_id())
            display_pokemon_info(pokemon_info)

def main():
    pokemon_app()


if __name__ == '__main__':
    main()


