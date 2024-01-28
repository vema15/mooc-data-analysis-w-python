#!/usr/bin/env python3
import pandas as pd
import numpy as np

def read_series():
    inds = []
    vals = []
    while True:
        user_input = input("")
        if user_input == "":
            break
        try:
            split_input = user_input.split()
            if len(split_input) == 2:
                inds.append(split_input[0])
                vals.append(split_input[1])
            else:
                raise Exception
        except:
            raise Exception
    return pd.Series(vals, index=inds)

def main():
    
    print(read_series())

if __name__ == "__main__":
    main()
