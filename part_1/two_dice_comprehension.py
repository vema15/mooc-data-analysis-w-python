#!/usr/bin/env python3

def main():
    combos = [(i+1, j+1) for i in range(6) for j in range(6) if ((i+1) + (j+1)) == 5]
    for i in combos:
        print(i)
if __name__ == "__main__":
    main()
