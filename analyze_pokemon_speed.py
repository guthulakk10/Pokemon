# Calculate the average speed of all Pokémon
average_speed = df['Speed'].mean()
print(f"The average speed of all starter Pokémon is {average_speed:.2f}.")

# Identify fast Pokémon (speed above average)
fast_pokemon = df[df['Speed'] > average_speed]
num_fast_pokemon = fast_pokemon.shape[0]
fast_pokemon_list = fast_pokemon['Pokemon'].tolist()

# Identify slow Pokémon (speed below average)
slow_pokemon = df[df['Speed'] < average_speed]
num_slow_pokemon = slow_pokemon.shape[0]
slow_pokemon_list = slow_pokemon['Pokemon'].tolist()

# Output results
print(f"The number of fast Pokémon is {num_fast_pokemon}.")
print(f"Fast Pokémon: {', '.join(fast_pokemon_list)}.")
