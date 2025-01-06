def calculate_average_stat(df, stat):
    if stat not in df.columns:
        raise ValueError(f"'{stat}' is not a valid column in the dataset.")
    
    return df[stat].mean()
