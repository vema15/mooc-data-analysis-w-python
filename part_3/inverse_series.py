#!/usr/bin/env python3
import numpy as np
import pandas as pd

def inverse_series(s):
    new_series = pd.Series(s.index, index=s.values)
    return new_series
def main():
    d = { 2001 : "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017 : "Trump"}
    s4 = pd.Series(d, name="Presidents")
    inverse_series(s4)

if __name__ == "__main__":
    main()
