#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df['LW'].replace('Re', None, inplace=True)
    df['LW'].replace('New', None, inplace=True)
    dropped_df = df.dropna(axis=0, how='any')
    return dropped_df[dropped_df['Pos'].astype(int) > dropped_df['LW'].astype(int)]


def main():
    special_missing_values()

if __name__ == "__main__":
    main()
