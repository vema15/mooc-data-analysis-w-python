#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def bicycle_timeseries():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(axis=0, how='all', inplace=True)
    df_split = df['Päivämäärä'].str.split(expand=True)
    df_split.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, inplace=True)
    df_split['Weekday'].replace({'ma': 1, 'ti': 2, 'ke': 3, 'to': 4, 'pe': 5, 'la': 6, 'su': 7}, inplace=True)
    df_split['Month'].replace({'tammi': '1', 'helmi': '2', 'maalis': '3', 'huhti': '4', 'touko': '5', 'kesä': '6', 'heinä': '7', 'elo': '8', 'syys': '9', 'loka': '10', 'marras': '11', 'joulu': '12'}, inplace=True)
    df_split['DatetimeIndex'] = df_split['Year'] + ' ' + df_split['Month'] + ' ' + df_split['Day'] + ' ' + df_split['Hour']
    df_split['DatetimeIndex'] = pd.to_datetime(df_split['DatetimeIndex'])
    concat = pd.concat([df_split, df], axis=1)
    concat.drop(columns=['Year', 'Month', 'Day', 'Hour', 'Päivämäärä', 'Unnamed: 21'], inplace=True)
    concat.set_index("DatetimeIndex", inplace=True)
    return concat

def commute():
    comm_data = bicycle_timeseries()
    aug_data = comm_data['2017-08-01':'2017-08-31']
    aug_week_days = aug_data.groupby('Weekday').sum()
    return aug_week_days
    
def main():
    week_data = commute()
    plt.gca().set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.plot(week_data)
    plt.show()


if __name__ == "__main__":
    main()
