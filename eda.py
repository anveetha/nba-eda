import pandas as pd

df = pd.read_csv("data/player_game_logs_2025_26.csv")

print(df.shape)

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())