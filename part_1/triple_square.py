#!/usr/bin/env python3
def triple(parameter: int):
        return parameter*3

def square(parameter: int):
        return parameter * parameter

def main():
    for i in range(10):
        if i == 0:
            triple(i)
            square(i)
            continue
        print(f'triple({i})=={i*3} square({i})=={i*i}')
        if triple(i+1) < square(i+1):
             break
if __name__ == "__main__":
    main()
