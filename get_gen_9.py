import requests
import json


def get_scarlet_violet():
    # Link for all Pokedex Regions
    get_link = 'https://pokeapi.co/api/v2/pokedex?limit=33'

    response = requests.get(get_link)
    pokedex_list = response.json()['results']

    target_regions = ['paldea', 'kitakami', 'blueberry']
    # Dict [name] -> [region url]
    target_region_urls = {}

    for region in pokedex_list:
        region_name = region['name']
        if region_name in target_regions:
            # Includes all region urls for target regions
            # Can edit based on which Pokemon are legal
            target_region_urls[region_name] = region['url']

    # Dict [name] -> [pokemon url]
    pokemon_entry_urls = {}
    pokemon_names = set()

    for region_name, url in target_region_urls.items():
        url_response = requests.get(url)
        region_data = url_response.json()

        print(f'Processing Region {region_data['name']}')
        print('-' * 40)

        entries = region_data['pokemon_entries']

        for entry in entries:
            pokemon_name = entry['pokemon_species']['name']
            pokemon_names.add(pokemon_name)

            pokemon_entry_urls[pokemon_name] = entry['pokemon_species']['url']




    # get_link = 'https://pokeapi.co/api/v2/pokemon?'

    # 2. Get all Pokemon and Filter out
    mythicals = ['Mew',
    'Jirachi',
    'Deoxys',
    'Phione',
    'Manaphy',
    'Darkrai',
    'Shaymin',
    'Arceus',
    'Keldeo',
    'Meloetta',
    'Diancie',
    'Hoopa',
    'Volcanion',
    'Magearna',
    'Zarude',
    'Pecharunt']

    res = 0

    for mythical in mythicals:
        if mythical in pokemon_names:
            res += 1

    print(res)
    print(len(mythicals))
    #There are no mythicals, filter another way

    #3. Turn them all into Pokemon class objects after import
    #Test Comment for Push

get_scarlet_violet()
