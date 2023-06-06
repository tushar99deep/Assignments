import requests
import json
import pandas as pd

def download_and_convert_to_excel():
    # Download the data from the provided link
    url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    response = requests.get(url)
    data = response.json()

    # Extract the required attributes from the data
    extracted_data = []
    for pokemon in data["pokemon"]:
        extracted_data.append({
            "id": pokemon["id"],
            "num": pokemon["num"],
            "name": pokemon["name"],
            "img": pokemon["img"],
            "type": ", ".join(pokemon["type"]),
            "height": pokemon["height"],
            "weight": pokemon["weight"],
            "candy": pokemon.get("candy", ""),
            "candy_count": pokemon.get("candy_count", ""),
            "egg": pokemon.get("egg", ""),
            "spawn_chance": pokemon.get("spawn_chance", ""),
            "avg_spawns": pokemon.get("avg_spawns", ""),
            "spawn_time": pokemon.get("spawn_time", ""),
            "multipliers": ", ".join(pokemon.get("multipliers", [])),
            "weakness": ", ".join(pokemon.get("weaknesses", [])),
            "next_evolution": ", ".join([evolution["name"] for evolution in pokemon.get("next_evolution", [])]),
            "prev_evolution": ", ".join([evolution["name"] for evolution in pokemon.get("prev_evolution", [])])
        })

    # Convert the extracted data into a DataFrame
    df = pd.DataFrame(extracted_data)

    # Save the DataFrame to an Excel file
    df.to_excel("pokemon_data.xlsx", index=False)
    print("Data has been converted and saved to 'pokemon_data.xlsx'.")

# Run the function to download, convert, and save the data
download_and_convert_to_excel()
