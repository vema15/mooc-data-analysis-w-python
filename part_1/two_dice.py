#!/usr/bin/env python3

def main():
    for i in range(6):
        for j in range(6):
            if ((i+1) + (j+1)) == 5:
                print((i+1, j+1))

if __name__ == "__main__":
    main()
