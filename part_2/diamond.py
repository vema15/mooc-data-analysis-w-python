#!/usr/bin/env python3

import numpy as np

def diamond(n):
    z = n + n-1
    p_holder = np.eye(n, dtype=int)
    p_holder_2 = np.concatenate((p_holder, p_holder))
    arranged_diamond = []
    cent_ind = z // 2
    new_array = np.zeros((z,z), dtype=int)
    for i in range(len(new_array)):
        if z % 2 == 0:
            cent_inds = [cent_ind-1, cent_ind]
            if i == 0 or i == len(new_array)-1:
                new_array[i][cent_inds[0]] = 1
                new_array[i][cent_inds[1]] = 1
            elif i > 0 and i < cent_inds[0]:
                new_array[i][cent_inds[0]-i] = 1
                new_array[i][cent_inds[1]+i] = 1
            elif i == cent_inds[0] or i == cent_inds[1]:
                new_array[i][0] = 1
                new_array[i][-1] = 1 
            elif i > cent_inds[1] and i < len(new_array)-1:
                new_array[i][i-cent_inds[1]] = 1
                new_array[i][-(i - cent_inds[0])] = 1
            arranged_diamond.append(np.array(new_array[i]))
        else:    
            if i == 0 or i == len(new_array)-1:
                new_array[i][cent_ind] = 1        
            elif i > 0 and i <= cent_ind:
                new_array[i][cent_ind-i] = 1
                new_array[i][cent_ind+i] = 1
            elif i > cent_ind and i < len(new_array)-1:
                new_array[i][i-cent_ind] = 1
                new_array[i][cent_ind-i-1] = 1
            arranged_diamond.append(np.array(new_array[i]))
    return np.array(arranged_diamond)

def main():
    print(diamond(2))

if __name__ == "__main__":
    main()
