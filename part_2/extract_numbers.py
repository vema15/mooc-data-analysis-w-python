#!/usr/bin/env python3

def extract_numbers(s):
    split_list = s.split(" ")
    new_list = []
    for i in split_list:
        try:
            new_list.append(int(i))
        except:
            try:
                new_list.append(float(i))
            except:
                continue
    return new_list
def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
