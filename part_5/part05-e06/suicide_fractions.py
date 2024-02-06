#!/usr/bin/env python3

import pandas as pd
import numpy as np

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df['sui/pop'] = (df['suicides_no']/df['population'])
    gf = df.groupby('country')['sui/pop'].mean()
    return gf

    

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
