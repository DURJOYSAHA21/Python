import pandas as pd
import requests
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as plt

data = {
    "Team": ["Warriors", "Raptors", "Lakers"],
    "Wins": [50, 48, 52],
    "Losses": [22, 24, 20]
}

df=pd.DataFrame(data)
print(df.head())
print(df[["Wins","Losses"]].mean())

url="https://jsonplaceholder.typicode.com/todos/1"
response =requests.get(url)
print("status code:", response.status_code)
data=response.json()
print(data)

all_teams=teams.get_teams()
print(all_teams[0])

teams_df=pd.DataFrame(all_teams)
pd.set_option("display.max_columns",None) # helps to see all col
print(teams_df.head())

print("")
ateam_row =teams_df[teams_df['nickname']=="Warriors"]
ateam_id=int(ateam_row['id'].iloc[0])
print(ateam_id)

gamefinder=leaguegamefinder.LeagueGameFinder(team_id_nullable=ateam_id)
games_df =gamefinder.get_data_frames()[0]
print(games_df.head())

# Home games (no @ symbol)
home_vs_raptors = games_df[games_df['MATCHUP'] == "GSW vs TOR"]

# Away games (with @ symbol)
away_vs_raptors = games_df[games_df['MATCHUP'] == "GSW @ TOR"]

print("Home games:\n", home_vs_raptors[['GAME_DATE','PLUS_MINUS']])
print("Away games:\n", away_vs_raptors[['GAME_DATE','PLUS_MINUS']])

plt.figure(figsize=(10,5)) #it sets width,height
plt.plot(home_vs_raptors ['GAME_DATE'],home_vs_raptors['PLUS_MINUS'],label="HOME VS RAPTORS",marker='o') 
plt.plot(away_vs_raptors['GAME_DATE'], away_vs_raptors['PLUS_MINUS'],  label="Away vs Raptors", marker='x')
plt.xticks(rotation=45)# rotate xlabels
plt.xlabel("Game Date")
plt.ylabel("PLUS_MINUS")
plt.title("Warriors vs Raptors: PLUS_MINUS")
plt.legend()
plt.show()