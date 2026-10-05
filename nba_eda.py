import pandas as pd
from nba_api.stats.endpoints import playergamelogs

SEASON = "2025-26"

print("Downloading NBA data...")

response = playergamelogs.PlayerGameLogs(
    season_nullable=SEASON,
    season_type_nullable="Regular Season",
    timeout=60
)

df = response.get_data_frames()[0]

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())


df.to_csv("data/player_game_logs_2025_26.csv", index=False)

print("Saved dataset!")