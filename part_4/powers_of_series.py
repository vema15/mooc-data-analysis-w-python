#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    data = []
    cols = [i+1 for i in range(k)]
    for i in range(len(s.index)):
        data.append([])
        for j in range(k):
            data[i].append(s[s.index[i]] ** (j+1))
    return pd.DataFrame(data, columns=cols, index=s.index)

    
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
