#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    munis = df[1:312]
    filtered_munis = munis[(munis["Share of Swedish-speakers of the population, %"] > 5) & (munis["Share of foreign citizens of the population, %"] > 5)]
    return filtered_munis[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
