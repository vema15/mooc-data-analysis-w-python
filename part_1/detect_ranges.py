#!/usr/bin/env python3

def detect_ranges(L):
    z = sorted(L)
    ranged_list = []
    counter = 0
    while counter <= len(z)-1:
        if counter+1 > len(L)-1:
            if type(ranged_list[-1]) == tuple and z[counter] != (ranged_list[-1][1]-1) or type(ranged_list[-1]) == int and z[counter] != ranged_list[-1]-1:
                ranged_list.append(z[-1])
            break
        if z[counter+1] != z[counter]+1:
            ranged_list.append(z[counter])
        else:
            temp_list = []
            temp_list.append(z[counter])
            for j in range(counter, len(z)):
                if j+1 > len(z)-1:
                    temp_list.append(z[j]+1)
                    counter = j
                    break
                if z[j+1] != z[j]+1:
                    temp_list.append(z[j]+1)
                    counter = j
                    break
            ranged_list.append(tuple(temp_list))
        counter += 1
    return ranged_list

def main():
    L = [4, 2, 0, -2, -4]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
