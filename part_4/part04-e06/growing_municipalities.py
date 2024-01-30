#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    denom = len(df.index)
    pos_growth = df[df["Population change from the previous year, %"] > 0]
    pctg = len(pos_growth.index)/denom
    return pctg

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t")[1:312]
    print(f'Proportion of growing municipalities: {(growing_municipalities(df) * 100):.1f}%')

if __name__ == "__main__":
    main()
