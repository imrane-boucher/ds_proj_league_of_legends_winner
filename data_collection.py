from riot_api import RiotAPI
import pandas as pd 

# get the full dataset
df = pd.read_csv('data/high_diamond_ranked_10min.csv')

# extract the column of gameIDs
gameIds = list(df['gameId'])



riotapi = RiotAPI('your api_key')

game_duration = []
for game_Id in gameIds:
    try:
        duration = riotapi.get_game_duration(game_Id)['gameDuration']
        game_duration.append(duration)
    # incase tu duration is missing for the specific match id
    except KeyError:
        print('nan value ...')
        duration = 0
        game_duration.append(duration)
        continue
    print(duration)

print('END')

df['GameDuration'] = game_duration

df.to_csv('./data/league_data_duration')