def Pokedex(df):
    while True:
        # Prompt the user for a Pokémon name
        name = input("What Pokémon would you like to know about? ").strip()
        selected_pokemon = df[df['Pokemon'].str.lower() == name.lower()]

        # Handle the case where the Pokémon is not found
        if selected_pokemon.empty:
            print(f"No Pokémon found with the name '{name}'.")
            continue  # Restart the loop

        # Prompt the user for the attribute they want to know
        info = input("What would you like to know about that Pokémon? ").strip()

        # Handle the special case for archetype
        if info.lower() in ['archetype', 'battle archetype']:
            print(get_archetype(df, name))  # Assuming get_archetype is defined elsewhere
            continue  # Restart the loop after providing the archetype

        # Check if the requested info is a valid column in the DataFrame
        if info not in df.columns:
            print(f"'{info}' is not a valid attribute of Pokémon.")
            continue  # Restart the loop if the attribute is invalid

        # Handle Type1 or Type2 specifically
        if info.lower() in ['type1', 'type2']:
            print(get_secondary_type(df, name))  # Assuming get_secondary_type is defined elsewhere
        else:
            # Extract and print the requested stat
            stat = selected_pokemon[info].iloc[0]
            print(f"The {info} of {name} is {stat}.")

        # Ask the user if they want to repeat the process
        repeat = input("Would you like to know about another Pokémon? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for using the Pokedex. See you later.")
            break
