#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def cyclists_per_day():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=1, how="all").dropna(axis=0, how='all')
    split_df = df['Päivämäärä'].str.split(expand=True)
    split_df = split_df.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"})
    split_df["Weekday"].replace(to_replace=["ma", 'ti', 'ke', 'to', 'pe', 'la', 'su'], value=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], inplace=True)
    split_df["Month"].replace(to_replace=['tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä', 'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu'], value=[i+1 for i in range(12)], inplace=True)
    rest = df.loc[:, 'Auroransilta':]
    total_df = pd.concat([split_df, rest], axis = 1)
    total_df = total_df.fillna(0)
    total_df.drop(columns=["Weekday", "Hour"], inplace=True)
    grouped = pd.DataFrame(total_df.groupby(["Day", "Month", "Year"]).sum())
    return grouped

def main():
    d_m_y = cyclists_per_day()
    z = d_m_y.groupby(["Year", "Month"])
    v = z.get_group(('2017', 8))
    v.plot()
    plt.show()        

    
if __name__ == "__main__":
    main()
