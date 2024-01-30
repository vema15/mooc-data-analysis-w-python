#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    def slice(x):
        if x[0:2][0] == '0':
            return x[0:2][1]
        else:
            return x[0:2]
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    split_times = df['Päivämäärä'].str.split(expand=True)
    split_times = split_times.dropna(axis=0)
    split_times = split_times.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"})
    split_times["Weekday"] = split_times["Weekday"].replace(to_replace= ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su'], value=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    split_times["Month"] = split_times["Month"].replace(to_replace=['tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä', 'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu'], value=['1', '2', '3','4','5','6','7','8','9','10','11','12'])
    hours_series = split_times['Hour'].apply(slice)
    split_times['Hour'] = hours_series
    split_times['Day'], split_times['Month'], split_times['Year'], split_times['Hour'] = split_times['Day'].astype(int), split_times['Month'].astype(int), split_times['Year'].astype(int), split_times['Hour'].astype(int)
    return split_times

def main():
    sd = split_date()
    print(sd)
       
if __name__ == "__main__":
    main()
