#!/usr/bin/env python3

import numpy as np
import scipy.linalg
import math

def vector_angles(X, Y):
    sum_dot_prod = np.sum(X * Y)
    x_vec_mag = np.sqrt(np.sum(X**2))
    y_vec_mag = np.sqrt(np.sum(Y**2))
    vec_rad = np.arccos((sum_dot_prod/(x_vec_mag * y_vec_mag)))
    return math.floor(float(vec_rad * 57.2958))

def main():
    #np.random.seed(0)
    #x = np.random.randint(1, 10, (4,4))
    #y = np.random.randint(1,10,(4,4))
    x = np.array([[0,0,1], [-1,1,0]])
    y = np.array([[0,1,0], [1,1,0]])
    print(vector_angles(x,y))

if __name__ == "__main__":
    main()
