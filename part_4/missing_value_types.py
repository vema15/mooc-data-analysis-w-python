#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    s1 = pd.Series(["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"])
    s2 = pd.Series([None, 1917, 1776, 1523, None, 1992])     
    s3 = pd.Series([None, "Niinistö", "Trump", None, "Steinmeier", "Putin"])                       
    df = pd.DataFrame({"State": s1, "Year of independence": s2, "President": s3})
    df.set_index('State', inplace=True)
    return df
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
