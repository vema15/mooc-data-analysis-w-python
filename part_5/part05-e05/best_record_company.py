#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df['tot_WoC'] = df.groupby("Publisher")['WoC'].transform('sum')
    df = df.sort_values('tot_WoC', ascending=False)
    top_pub = df[0:1]["Publisher"].tolist()[0]
    top_list = df[df["Publisher"] == top_pub]
    return top_list.drop(columns="tot_WoC")


    
    

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
