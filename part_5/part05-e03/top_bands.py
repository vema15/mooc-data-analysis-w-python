#!/usr/bin/env python3

import pandas as pd

def top_bands():
    top_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    band_df = pd.read_csv("src/bands.tsv", sep="\t")
    band_df['Band'] = band_df['Band'].str.upper()
    return pd.merge(band_df, top_df, left_on="Band", right_on="Artist")
    

def main():
    print(top_bands())

if __name__ == "__main__":
    main()
