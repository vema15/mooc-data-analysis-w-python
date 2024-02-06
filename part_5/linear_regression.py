#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)
    lr_mdl = LinearRegression()
    lr_mdl.fit(x, y)
    return lr_mdl.coef_[0][0], lr_mdl.intercept_[0]

    
def main():
    x = np.array([3, 8, 9, 5, 4])
    y = np.array([9, 5, 7, 7, 4])
    coef, inter = fit_line(y, x)
    print(f'Slope: {coef}')
    print(f'Intercept: {inter}')
    plt.axline(xy1 = (0, inter), slope=coef, label=f'$y = {coef:.1f}x {inter:+.1f}$')
    plt.plot(x, y, 'o')
    plt.plot(x, y, 'o')
    plt.show()
if __name__ == "__main__":
    main()
