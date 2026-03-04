import pandas as pd

def transform_games():
    print("Transforming the data...")
    
    # Read the CSV file created by the scraper
    df = pd.read_csv("data/raw/aris_games.csv")
    
    # Add a column: did Aris win or not?
    # Check if Aris was the home or away team and compare scores
    def aris_won(row):
        if row["home_team"] == "Aris":
            return row["home_score"] > row["away_score"]
        else:
            return row["away_score"] > row["home_score"]
    
    df["aris_won"] = df.apply(aris_won, axis=1)
    
    # Add a column: Aris's score in each game
    df["aris_score"] = df.apply(
        lambda row: row["home_score"] if row["home_team"] == "Aris" 
        else row["away_score"], axis=1
    )
    
    # Add a column: opponent's score
    df["opponent_score"] = df.apply(
        lambda row: row["away_score"] if row["home_team"] == "Aris" 
        else row["home_score"], axis=1
    )
    
    # Add a column: opponent's name
    df["opponent"] = df.apply(
        lambda row: row["away_team"] if row["home_team"] == "Aris" 
        else row["home_team"], axis=1
    )
    
    # Save to the processed folder
    df.to_csv("data/processed/aris_games_processed.csv", index=False)
    print("Data saved to data/processed/aris_games_processed.csv!")
    
    # Print basic statistics
    wins = df["aris_won"].sum()
    losses = len(df) - wins
    print(f"\nTotal games: {len(df)}")
    print(f"Wins: {wins} | Losses: {losses}")
    print(f"Average points: {df['aris_score'].mean():.1f}")
    
    return df

if __name__ == "__main__":
    transform_games()
