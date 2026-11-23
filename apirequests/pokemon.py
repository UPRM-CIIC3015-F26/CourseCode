import json
import requests


# Slide 6: Basic requests pattern (reading response.text)
def basic_request():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    result = requests.get(url)
    if result.status_code == 200:
        contents = result.text
        print(contents[:300], "...")  # Truncated for readability in class
    else:
        print("Error:", result.status_code)


# Slide 7: Working requests program (decoding JSON & navigating dicts/lists)
def working_json_request():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    result = requests.get(url)
    if result.status_code == 200:
        data = result.json()
        print("Primary type:", data["types"][0]["type"]["name"])
        print("Species URL:", data["species"]["url"])
    else:
        print("Request failed:", result.status_code)


# Slide 11: Making GET requests with params and headers
def get_with_params_and_headers():
    # Simple GET
    res = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    print("Simple GET status:", res.status_code)

    # GET with query params -> https://pokeapi.co/api/v2/pokemon?limit=10&offset=20
    my_params = {"limit": 10, "offset": 20}
    res = requests.get("https://pokeapi.co/api/v2/pokemon", params=my_params)
    if res.status_code == 200:
        print("Request URL:", res.url)
        names = [p["name"] for p in res.json()["results"]]
        print("Pokemon (offset 20, limit 10):", names)

    # GET with custom headers
    my_headers = {"User-Agent": "pokedex-app"}
    res = requests.get(
        "https://pokeapi.co/api/v2/pokemon-species/25", headers=my_headers
    )
    if res.status_code == 200:
        print("Species name:", res.json()["name"])


# Slide 15: Checking response status codes
def check_status_codes():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        print("Found:", data["name"])
    elif res.status_code == 404:
        print("Pokemon not found (404)")
    else:
        print(f"Request failed: {res.status_code}")


# Slide 17: Handling request & status errors
def handle_request_errors():
    url = "https://pokeapi.co/api/v2/pokemon/missingno"
    res = requests.get(url)
    if res.status_code == 200:
        print(res.json()["name"])
    elif res.status_code == 400:
        print("Bad request (400): check URL or params")
    elif res.status_code == 404:
        print("Pokemon not found (404)")
    elif res.status_code == 429:
        print("Rate limited (429): slow down requests")
    else:
        print(f"Unexpected status code: {res.status_code}")


# Slide 20: Using JSON in Python (res.json, json.loads, json.dumps)
def using_json_in_python():
    # 1. From an API response
    res = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    if res.status_code == 200:
        poke_dict = res.json()  # JSON -> Python dict
        print("From API:", poke_dict["name"], poke_dict["id"])

    # 2. From a JSON string (json.loads)
    raw_text = '{"name": "bulbasaur", "id": 1}'
    entry = json.loads(raw_text)
    print("From json.loads:", entry["name"])  # "bulbasaur"

    # 3. Convert Python dict -> JSON string (json.dumps)
    json_str = json.dumps(entry, indent=2)
    print("From json.dumps:\n" + json_str)


# Slide 22: Direct chained PokéAPI requests (fetch species lore & evolution URL)
def fetch_species_info(species_url):
    res = requests.get(species_url)
    if res.status_code != 200:
        return {"lore": "No lore.", "evolution_chain_url": ""}
    data = res.json()
    lore = "No English Pokédex entry available."
    for entry in data["flavor_text_entries"]:
        if entry["language"]["name"] == "en":
            text = entry["flavor_text"]
            lore = text.replace("\n", " ").replace("\f", " ").strip()
            break
    return {
        "lore": lore,
        "evolution_chain_url": data["evolution_chain"]["url"],
    }


# Slide 23: Recursive tree traversal for evolution chain
def extract_evolution_names(chain_node):
    names = [chain_node["species"]["name"]]
    for next_node in chain_node["evolves_to"]:
        names.extend(extract_evolution_names(next_node))
    return names


# Slides 22 & 23: Full chained request demo (/pokemon -> species -> evolution_chain)
def chained_requests_and_evolutions(pokemon_name="pikachu"):
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if res.status_code != 200:
        print(f"Failed to fetch {pokemon_name}: {res.status_code}")
        return

    species_url = res.json()["species"]["url"]
    species_info = fetch_species_info(species_url)
    print("Lore:", species_info["lore"])

    evo_url = species_info["evolution_chain_url"]
    if evo_url:
        evo_res = requests.get(evo_url)
        if evo_res.status_code == 200:
            chain_root = evo_res.json()["chain"]
            evolutions = extract_evolution_names(chain_root)
            print("Evolution chain:", evolutions)


# Uncomment the example you want to show during class:

# basic_request()
working_json_request()
# get_with_params_and_headers()
# check_status_codes()
# handle_request_errors()
# using_json_in_python()
# chained_requests_and_evolutions("pikachu")
# chained_requests_and_evolutions("eevee")
