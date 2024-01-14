#!/usr/bin/env python3

def distinct_characters(L):
    distinct_dict = {}
    for string in L:
        if string not in distinct_dict:
            distinct_dict[f'{string}'] = len(set(string))
    return distinct_dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
