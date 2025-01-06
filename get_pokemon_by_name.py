def get_pokemon_by_name(df, pokemon_name):
  
    # Filter the DataFrame by the 'Pokemon' name (case-insensitive)
    selected_pokemon = df[df['Pokemon'].str.lower() == pokemon_name.lower()]

    # If no Pokémon matches the name, return a friendly message
    if selected_pokemon.empty:
        return f"No Pokémon found with the name '{pokemon_name}'."

    # Return the row of the Pokémon with the matching name
    return selected_pokemon
