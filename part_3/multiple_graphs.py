#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    x1_vals = np.array([2,4,6,7])
    y1_vals = np.array([4,3,5,1])
    x2_vals = np.array([1,2,3,4])
    y2_vals = np.array([4,2,3,1])
    plt.plot(x1_vals, y1_vals, label = "data-1")
    plt.plot(x2_vals, y2_vals, label = "data-2")
    plt.title("title")
    plt.ylabel("y-axis")
    plt.xlabel("x-axis")
    plt.show()

if __name__ == "__main__":
    main()
