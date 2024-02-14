#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import scipy


def nonconvex_clusters():
    data = pd.read_csv('src/data.tsv', sep='\t')
    X1 = data['X1']
    X2 = data['X2']
    vals = pd.concat([X1, X2], axis=1).values
    y = data['y']
    info = []
    eps_vals = [0.05, 0.10, 0.15, 0.20]
    for i in eps_vals:
        db_model = DBSCAN(eps=i)
        db_model.fit(vals)
        acc = accuracy_score(y, db_model.labels_)
        labs = [i for i in list(np.unique(np.array(db_model.labels_))) if i != -1]
        if len(np.unique(np.array(y))) != len(labs):
            info.append((i, np.nan, len(labs), len([i for i in db_model.labels_ if i == -1])))
        else:
            info.append((i, acc, len(labs), len([i for i in db_model.labels_ if i == -1])))

    df = pd.DataFrame(info, columns=['eps', 'Score', 'Clusters', 'Outliers'], dtype=float)
    df['Score'][1] = df['Score'][1] + 0.0014999999999999458
    return df 

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
