import os

# General packages
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from IPython.display import Image, display
import math

'''
RangeIndex: 112 entries, 0 to 111
Data columns (total 34 columns):
 #   Column                                           Non-Null Count  Dtype
---  ------                                           --------------  -----
 0   Rk (Ranking out of Quarterbacks)                 111 non-null    float64
 1   Player (Name of Player)                          112 non-null    object
 2   Age (Age of Player)                              111 non-null    float64
 3   Team (Team of Player)                            111 non-null    object
 4   Pos (Position of Player)                         111 non-null    object
 5   G (Games Played)                                 111 non-null    float64
 6   GS (Games Started as Off/Def player)             111 non-null    float64
 7   QBrec (Team Record in games started)             59 non-null     object
 8   Cmp (Passes completed)                           111 non-null    float64
 9   Att (Passes attempted)                           111 non-null    float64
 10  Cmp% (Percentage of Passes Completed)            106 non-null    float64
 11  Yds (Yards gained by passing)                    111 non-null    float64
 12  TD (Passing Touchdowns)                          111 non-null    float64
 13  TD% (Percentage of TDs thrown when passing)      106 non-null    float64
 14  Int (Interceptions)                              111 non-null    float64
 15  Int% (Percentage of INTs when throwing a pass)   106 non-null    float64
 16  1D (First Downs Passing)                         111 non-null    float64
 17  Succ% (Passing Success Rate)                     90 non-null     float64
 18  Lng (Longest Completed Pass Thrown)              92 non-null     float64
 19  Y/A (Yards Gained per Pass Attempt)              106 non-null    float64
 20  AY/A (Adjusted Yards gained through pass attempt)106 non-null    float64
 21  Y/C (Yards gained through pass completion)       93 non-null     float64
 22  Y/G (yards gained through game played)           112 non-null    float64
 23  Rate (Passer Rating)               106 non-null    float64
 24  QBR (Quarterback Rating)               99 non-null     float64
 25  Sk (Times Sacked)                111 non-null    float64
 26  Yds_1 (Yards Lost due to sacks)             111 non-null    float64
 27  Sk% (Percentage of times sacked when passing)                112 non-null    float64
 28  NY/A (Net Yards gained from pass atempt)               112 non-null    float64
 29  ANY/A (Adjusted Net Yards gained from pass attemp)              112 non-null    float64
 30  4QC (4th Quarter Comebacks Led)                111 non-null    float64
 31  GWD (Game Winning Drives Led by QB)                111 non-null    float64
 32  Awards (Awards)             26 non-null     object
 33  Player-additional (Additional Player infos)  112 non-null    object
dtypes: float64(28), object(6)
memory usage: 29.9+ KB


'''



qb_data = pd.read_csv('QB_2024.csv')

#Dropping unnecessary columns:

print(qb_data.info())

# #Clean up any rows with no values: Nan
# team_data.dropna(axis=0, inplace=True)



#remove all stats before 2003 season
print(qb_data.columns.values)
