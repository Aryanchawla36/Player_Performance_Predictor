import os

# General packages
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from IPython.display import Image, display

'''
Weather Data Info 

RangeIndex: 11192 entries, 0 to 11191
Data columns (total 11 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   id           11192 non-null  object   
 1   home_team    11192 non-null  object 
 2   home_score   11192 non-null  int64  
 3   away_team    11192 non-null  object 
 4   away_score   11192 non-null  int64  
 5   temperature  11192 non-null  int64  
 6   wind_chill   1617 non-null   float64
 7   humidity     9285 non-null   object 
 8   wind_mph     9347 non-null   float64
 9   weather      11192 non-null  object 
 10  date         11192 non-null  object 

'''



weather_data = pd.read_csv('datasets\weather_20131231.csv')

##Cleaning Data

#Dropping weather for redundancy
weather_data = weather_data.drop(columns=['weather'])
#Dropping windchill as there is not enough data
weather_data = weather_data.drop(columns=['wind_chill'])
# Strip '%' from humidity column and convert to numeric
weather_data['humidity'] = weather_data['humidity'].str.rstrip('%').astype(float) / 100
weather_data['date'] = pd.to_datetime(weather_data['date'])
#Normalizing Features:
scaler = MinMaxScaler()
weather_data[['temperature', 'humidity', 'wind_mph']] = scaler.fit_transform(
    weather_data[['temperature', 'humidity', 'wind_mph']]
)

weather_data.to_csv('cleaned_weather_data.csv', index=False)
