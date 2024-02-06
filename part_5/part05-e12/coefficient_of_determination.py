#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def coefficient_of_determination():
    read_mys_data = pd.read_csv('src/mystery_data.tsv', sep='\t')
    x_cols = read_mys_data.drop('Y', axis=1)
    y = read_mys_data['Y']
    lr_model = LinearRegression(fit_intercept=False)
    x = np.vstack(x_cols.values)
    lr_model.fit(x, y)
    all_scores = [lr_model.score(x, y)]
    for i in x_cols:
        lr_other = LinearRegression()
        lr_other.fit(np.array(read_mys_data[i]).reshape(-1,1), np.array(y).reshape(-1, 1))
        all_scores.append(lr_other.score(np.array(read_mys_data[i]).reshape(-1,1), np.array(y).reshape(-1, 1)))
    return all_scores
def main():
    r2_scores = coefficient_of_determination()
    for i in range(len(r2_scores)):
        if i == 0:
            print(f"R2-score with features(s) X: {r2_scores[i]}")
        else:
            print(f'R2-score with feature(s) X{i}: {r2_scores[i]}')


if __name__ == "__main__":
    main()
