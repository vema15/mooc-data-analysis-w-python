#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    read_csv = load()
    x_y = np.array([read_csv[:, 0], read_csv[:, 2]]).T
    return scipy.stats.pearsonr(x_y[:, 0], x_y[:, 1])[0]

def correlations():
    read_csv = load()
    pear_corr_list = []
    for i in range(len(read_csv[0])):
        row_corrs = []
        for j in range(len(read_csv[0])):
            row_corrs.append(scipy.stats.pearsonr(read_csv[:, i], read_csv[:, j])[0])
            np.corrcoef(read_csv[:, i])
        pear_corr_list.append(row_corrs)
    return np.array(pear_corr_list)
    

def main():
    #print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
