#!/usr/bin/env python3
import numpy as np
import functools

def matrix_power(a, n):
    lis = [1, 3, 5, 6, 2] 
    functools.reduce(lambda a, b: a+b, lis)
    if n >= 1:
        z = np.linalg.matrix_power(a, n)
    elif n == 0:
        return np.eye(a.shape[0], dtype=int)
    else:
        if n == -1:
            return np.linalg.inv(a)
        else:
            return np.linalg.matrix_power(np.linalg.inv(a), -n)
    return z
def main():
    a = np.array([[3,3,3],
                 [3,3,3],
                 [3,3,3]])
    b = np.array([[1,2],
                  [3,4]])
    print(matrix_power(b, 0))

if __name__ == "__main__":
    main()
