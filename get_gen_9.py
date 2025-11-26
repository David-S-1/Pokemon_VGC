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

        entries = region_data['pokemon_entries']

        for entry in entries:
            pokemon_name = entry['pokemon_species']['name']
            pokemon_names.add(pokemon_name)

            pokemon_entry_urls[pokemon_name] = pokemon_entry_urls[
                pokemon_name] = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            # This link gets important stats, abilties, etc. about the Pokemon

    banned_mythicals = ['mew',
                        'jirachi',
                        'deoxys',
                        'phione',
                        'manaphy',
                        'darkrai',
                        'shaymin',
                        'arceus',
                        'keldeo',
                        'meloetta',
                        'hoopa',
                        'diancie',
                        'volcanion',
                        'magearna',
                        'zarude',
                        'pecharunt']

    for mythical in banned_mythicals:
        if mythical in pokemon_names:
            pokemon_names.remove(mythical)

    #Add Regulations (WIP)
    #Cache Pokemon Data (Taking a long time to load)

    #3. Turn them all into Pokemon class objects after import
    #Test Comment for Push
    return [pokemon_names, pokemon_entry_urls]
