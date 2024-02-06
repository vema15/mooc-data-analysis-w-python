#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def cycling_weather_continues(station):
    #Transform Pai to be compatible with dates
    stat_df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    stat_df.dropna(axis=0, how='all', inplace=True)
    stat_df.dropna(axis=1, how='all', inplace=True)
    stat_df = stat_df.fillna(value=0)
    date_df = stat_df['Päivämäärä'].str.split(expand=True)
    stat_df.drop(columns=['Päivämäärä'], inplace=True)
    date_df.drop(columns=[0, 4], inplace=True)
    date_df.rename(columns={1: "Day", 2: "Month", 3: "Year"}, inplace=True)
    date_df['Year'] = date_df['Year'].astype(int)
    date_df['Day'] = date_df['Day'].astype(int)
    date_df['Month'].replace(to_replace=['tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä', 'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu'], value=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], inplace=True)
    
    #Group station data by every day of the year
    your_station = stat_df[station]
    date_df['Station'] = your_station
    date_df.dropna(axis=0, how='any', inplace=True)
    date_df.fillna(0, inplace=True)
    date_df_2017 = date_df.loc[date_df['Year'] == 2017]
    grouped_2017 = date_df_2017.groupby(['Year', 'Month', 'Day']).sum()
    grouped_2017 = grouped_2017.reset_index()
    
    #Get Weather data
    weather_df = pd.read_csv('src/kumpula-weather-2017.csv')
    weather_df['Snow depth (cm)'].replace(to_replace=-1, value=0, inplace=True)
    weather_df = weather_df.fillna(value=0)

    #Join weather and station data
    merged_df = pd.merge(grouped_2017, weather_df, left_on=['Year', 'Month', 'Day'], right_on=['Year', 'm', 'd'])
    merged_df.drop(columns=['m','d','Time','Time zone'], inplace=True)
   
    #Gather explanatory and response variables
    exp_vars = np.array([merged_df['Precipitation amount (mm)'], merged_df['Snow depth (cm)'], merged_df['Air temperature (degC)']]).T
    resp_var = np.array([merged_df['Station']]).T
    lr_model = LinearRegression()
    lr_model.fit(exp_vars, resp_var)
    coefs = lr_model.coef_
    r_score = lr_model.score(exp_vars, resp_var)
    return list(coefs[0]), r_score
    
def main():
    station = 'Merikannontie'
    cyc_weath_data = cycling_weather_continues(station)
    print(f'Measuring station: {station}')
    print(f"Regression coefficient for variable 'precipitation': {cyc_weath_data[0][0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {cyc_weath_data[0][1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {cyc_weath_data[0][2]:.1f}")
    print(f'Score: {cyc_weath_data[1]:.2f}') 

if __name__ == "__main__":
    main()



