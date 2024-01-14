#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed_dict = {}
    for key, value in d.items():
        for word in value:
            if word not in reversed_dict:
                reversed_dict[word] = [] 
    for key, value in d.items():
        for word in value:
            if word in reversed_dict:
                reversed_dict[word].append(key)
    return reversed_dict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
