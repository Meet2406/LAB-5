'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/charmander'

def main():
    # Test out the get_pokemon_info() function
    poke_info = get_pokemon_info("charmander")
    print(poke_info, end ='\n\n')
    # Use breakpoints to view returned dictionary
    
    
    
    

def get_pokemon_info(pokemon_name):
    pokemon_name = str (pokemon_name).strip().lower()
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    #Todo: Clean the Pokemon name parameter
    headers = {
        'Accept': 'aplication/json'  
    }
    # Todo: Build a clean URL and use it to send a GET request
    print(f'Getting random pokeapi...', end='')
    url= POKE_API_URL + 'charmander'
    resp_msg = requests.get(url, headers=headers)
    

    #Todo: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        return resp_msg.json()
    # Todo: If the GET request failed, print the error reason and return None
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')         
        return
    

if __name__ == '__main__':
    main()