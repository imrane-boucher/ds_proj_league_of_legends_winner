# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:19:39 2020

@author: imran
"""

# Necessary librairies
import pandas as pd

# The first step of the project is the explore & clean the data, as well as 
# understanding the various features available to later make our prediction 
# I also want to forsee which features I can potentially later engeener as well
# as noticing if the data needs mean normalization or feature 

# import the data

# the base data is a ready to use dataset available on kaggle :
# https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min

# import extended data w/ game duration
df = pd.read_csv('data/league_data_duration.csv')


# over 7300 missing game durations 
# clean the data by removing the games (rows) where the game duration is missing
df = df[df['GameDuration'] != 0]

# Turn Game Duration from seconds into minutes
df['GameDuration'] = round(df['GameDuration'] / 60,0)
print(df.head())
# save the new data set with 2500 rows
df.to_csv('./data/league_data_cleaned_10min.csv', encoding='utf-8', index=False)

# there's no null values and only numerical data, the dataset seems already ready
# for modelling 

# the data contains 40 columns, 18 feature for each team, which means that some 
# features are redundant. The big part of the job will therefore be feature
# selection & feature engeeniring.

# some features are useless in the prediction:
    # - gameId 
    # - blueTowersDestroyed (it is a pretty rare event before 10 min of game
    # but can it have a powerful prediction effect? we need to analyze further
    # this variable)
    # redTotalGold & BlueTotalGold are well summarized by blueGoldDiff (we also don't need redGoldDiff)
    # blueTotalExperience & redExperienceDiff can be replaced by BlueExperienceDiff 
    # (we also don't need redExperienceDiff)
    # we don't need RedFirstBlood (only BlueFirstBlood)
    # ...
    
# we can engeener some features by replacing for instance Red/BlueTtotalJungleMinionsKilled
# by blueDiffJungleMinionsKilled

