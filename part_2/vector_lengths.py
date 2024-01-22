#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    length = np.sqrt(np.sum((a**2), axis=1))
    return length

def main():
    np.random.seed(0)
    test_array = np.random.randint(1, 10, (10,5))
    vector_lengths(test_array)

if __name__ == "__main__":
    main()
