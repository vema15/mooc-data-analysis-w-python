#!/usr/bin/env python3

def merge(L1, L2):
    L = L1+L2
    def sort_alg(x: list):
        is_sorted = False
        for i in range(len(x)):
            if i+1 > len(x)-1:
                break
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
        for i in range(len(x)):
            if i+1 > len(x)-1:
                break
            if x[i] > x[i+1]:
                is_sorted = False
                break
            else:
                is_sorted = True
        if is_sorted == True:
            return x
        else:
            sort_alg(x)
    sort_alg(L)    
    return L
def main():
    L1 = [1,7,3,4]
    L2 = [5,3,4,2]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
