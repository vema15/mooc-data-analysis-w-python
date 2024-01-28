#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    values = np.array(np.stack([list(np.unique(a[:, c], return_counts=True)[0]), list(np.unique(a[:, c], return_counts=True)[1])])).T
    print(values)
    sorted_vals = values[values[:, 1].argsort()[::-1]]
    sorted_dict = {}
    for i in range(len(list(sorted_vals))):
        sorted_dict[int(sorted_vals[i][0])] = sorted_vals[i][1]
    true_sorted = dict(sorted(sorted_dict.items(), key=lambda x:x[1], reverse=True))
    row_rank = []
    for i in range(len(a)):
        if a[i][c] in true_sorted:
            row_rank.append([a[i], true_sorted[a[i][c]]])
        else:
            row_rank.append([a[i], 0])
    sorted_col = sorted(row_rank, key=lambda x:x[1])
    return np.array([i[0] for i in reversed(sorted_col)])


        
    
    
    

def main():
    a = np.array([[5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
                  [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
                  [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
                  [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
                  [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
                  [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
                  [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
                  [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
                  [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
                  [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]])
    b = np.array([[9, 8, 4, 6, 6, 0, 5, 9, 3, 6],
                  [1, 0, 6, 7, 8, 7, 9, 8, 9, 1],
                  [5, 6, 5, 6, 5, 5, 1, 0, 5, 5],
                  [6, 0, 8, 9, 6, 4, 0, 2, 6, 9],
                  [1, 4, 6, 1, 5, 0, 9, 5, 4, 5],
                  [6, 7, 9, 1, 7, 8, 7, 5, 6, 2],
                  [8, 6, 2, 1, 0, 1, 1, 0, 6, 2],
                  [9, 7, 1, 5, 1, 5, 6, 0, 1, 8],
                  [2, 6, 1, 4, 1, 9, 5, 2, 2, 0],
                  [5, 9, 2, 9, 4, 3, 0, 8, 7, 4]])
    print(most_frequent_first(b, 0))

if __name__ == "__main__":
    main()
