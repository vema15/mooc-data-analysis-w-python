#!/usr/bin/env python3

import pandas as pd


def bicycle_timeseries():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(axis=0, how='all', inplace=True)
    df_split = df['Päivämäärä'].str.split(expand=True)
    df_split.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, inplace=True)
    df_split['Weekday'].replace({'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}, inplace=True)
    df_split['Month'].replace({'tammi': '1', 'helmi': '2', 'maalis': '3', 'huhti': '4', 'touko': '5', 'kesä': '6', 'heinä': '7', 'elo': '8', 'syys': '9', 'loka': '10', 'marras': '11', 'joulu': '12'}, inplace=True)
    df_split.drop(columns=['Weekday'], inplace=True)
    df_split['DatetimeIndex'] = df_split['Year'] + ' ' + df_split['Month'] + ' ' + df_split['Day'] + ' ' + df_split['Hour']
    df_split['DatetimeIndex'] = pd.to_datetime(df_split['DatetimeIndex'])
    concat = pd.concat([df_split, df], axis=1)
    concat.drop(columns=['Year', 'Month', 'Day', 'Hour', 'Päivämäärä', 'Unnamed: 21'], inplace=True)
    concat.set_index("DatetimeIndex", inplace=True)
    return concat

def main():
    bicycle_timeseries()

if __name__ == "__main__":
    main()
