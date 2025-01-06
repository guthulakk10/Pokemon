def get_secondary_type(df, name):
    selected_pokemon = df[df['Pokemon'].str.lower() == name.lower()]

    # If no Pokémon matches the name, return a friendly message
    if selected_pokemon.empty:
        return f"No Pokémon found with the name '{name}'."

    # Extract primary and secondary types
    primary_type = selected_pokemon['Type1'].iloc[0]
    secondary_type = selected_pokemon['Type2'].iloc[0]

    # Check if the secondary type is missing (NaN)
    if pd.isnull(secondary_type):
        return f"The Pokémon {name} is purely a {primary_type}-type Pokémon."
    else:
        return f"The Pokémon {name} is a {primary_type}-type and a {secondary_type}-type Pokémon."
