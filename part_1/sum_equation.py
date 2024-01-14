#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    res_string = ''
    for i in L:
        if i == L[-1]:
            res_string+=f"{str(i)} = "
        else:
            res_string+=f"{str(i)} + "
    return res_string + f"{str(sum(L))}"
    

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
