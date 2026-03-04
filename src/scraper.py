import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_BASKETBALL_KEY")

auth_headers = {
    "x-apisports-key": API_KEY
}

ARIS_ID = 606

def get_aris_games():
    print("Fetching games for Aris...")
    
    url = "https://v1.basketball.api-sports.io/games"
    params = {
        "team": ARIS_ID,
        "season": "2024-2025"
    }
    
    response = requests.get(url, headers=auth_headers, params=params)
    data = response.json()
    
    print(f"found {data['results']} matches!")
    
    games_list = []
    for game in data["response"]:
        games_list.append({
            "date": game["date"][:10],
            "home_team": game["teams"]["home"]["name"],
            "away_team": game["teams"]["away"]["name"],
            "home_score": game["scores"]["home"]["total"],
            "away_score": game["scores"]["away"]["total"],
            "league": game["league"]["name"]
        })
    
    df = pd.DataFrame(games_list)
    df.to_csv("data/raw/aris_games.csv", index=False)
    print("Data saved to data/raw/aris_games.csv!")
    
    return df

if __name__ == "__main__":
    get_aris_games()