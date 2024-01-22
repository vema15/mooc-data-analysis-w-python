#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    factors = np.arange((n))
    reshaped = factors.reshape((n,1))
    return reshaped * np.arange(n)

    

def main():
    print(multiplication_table(5))

if __name__ == "__main__":
    main()
