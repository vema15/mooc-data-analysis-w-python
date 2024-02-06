#!/usr/bin/env python3

import pandas as pd

def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    def slice(x):
        if x[0:2][0] == '0':
            return x[0:2][1]
        else:
            return x[0:2]
    split_times = df['Päivämäärä'].str.split(expand=True)
    split_times = split_times.dropna(axis=0)
    split_times = split_times.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"})
    split_times["Weekday"] = split_times["Weekday"].replace(to_replace= ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su'], value=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    split_times["Month"] = split_times["Month"].replace(to_replace=['tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä', 'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu'], value=['1', '2', '3','4','5','6','7','8','9','10','11','12'])
    hours_series = split_times['Hour'].apply(slice)
    split_times['Hour'] = hours_series
    split_times['Day'], split_times['Month'], split_times['Year'], split_times['Hour'] = split_times['Day'].astype(int), split_times['Month'].astype(int), split_times['Year'].astype(int), split_times['Hour'].astype(int)
    
    rest = df.loc[:, "Auroransilta":"Baana"]
    rest.dropna(how="all", axis=0, inplace=True)
    return pd.concat([split_times, rest], axis=1)

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
