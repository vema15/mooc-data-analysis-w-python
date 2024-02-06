#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def mystery_data():
    read_mys_data = pd.read_csv('src/mystery_data.tsv', sep='\t')
    x_cols = read_mys_data.drop('Y', axis=1)
    y = read_mys_data['Y']
    lr_model = LinearRegression(fit_intercept=False)
    x = np.vstack(x_cols.values)
    lr_model.fit(x, y)
    return lr_model.coef_

def main():
    coefficients = mystery_data()
    for c in range(len(coefficients)):
        print(f'Coefficient of X{c+1} is {coefficients[c]}')
    
    
if __name__ == "__main__":
    main()
