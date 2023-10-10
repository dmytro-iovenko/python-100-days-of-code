import pandas as pd

# reading 1 csv file from the website
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

# rename columns
df_premier21 = df_premier21.rename(columns={'Date':'date',
                                            'HomeTeam':'home_team',
                                            'AwayTeam':'away_team',
                                            'FTHG': 'home_goals',
                                            'FTAG': 'away_goals'})