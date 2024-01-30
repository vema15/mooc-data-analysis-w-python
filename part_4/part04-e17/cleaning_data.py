#!/usr/bin/env python3

import pandas as pd
import numpy as np

def start_slice(x):
    if len(x) > 4:
        return x[0:4]
    return x 
def pres_arrange(x):
    if "," in x:
        split_val = x.split(",")
        return split_val[1][1:len(split_val[1])].capitalize()+ " " + split_val[0].capitalize()
    else:
        split_val = x.split()
        return split_val[0].capitalize() + " " + split_val[1].capitalize()
        

def seasons(x):
    num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    try:
        return int(x)
    except:
        return num_dict[x]
    

def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    df["President"] = df["President"].apply(pres_arrange)
    df["Start"] = df["Start"].apply(start_slice).astype(int)
    df["Last"] = pd.to_numeric(df["Last"], errors="coerce")
    df["Seasons"] = df["Seasons"].apply(seasons).astype(int)
    df["Vice-president"] = df["Vice-president"].apply(pres_arrange)
    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
