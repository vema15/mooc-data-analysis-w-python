#!/usr/bin/env python3


def main():
    for i in range(10):   
        for j in range(10):
            cell_num = (i+1) * (j+1)
            print(f'{" "*(4-len(str(cell_num)))}{cell_num}', end="")
        print()

if __name__ == "__main__":
    main()