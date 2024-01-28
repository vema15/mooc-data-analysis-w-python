#!/usr/bin/env python3
import numpy as np
import pandas as pd

def create_series(L1, L2):
    indices = ["a", "b", "c"]
    return (pd.Series(L1, index=indices), pd.Series(L2, index=indices))
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    s1 + s2
    return s1, s2
    
def main():
    L1 = [1,2,3]
    L2 = [4,5,6]
    S1, S2 = create_series(L1, L2)
    modify_series(S1, S2)
    
if __name__ == "__main__":
    main()
