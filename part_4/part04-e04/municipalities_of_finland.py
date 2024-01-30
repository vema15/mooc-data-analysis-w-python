#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    end = df.index.get_indexer(["Äänekoski"])[0]+1
    df_new = pd.DataFrame(df[1:end])
    return df_new
   
    
    #print(df[1:
        

    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
