#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    #newstr = re.findall(r"([-]?\d+)", s)
    newstr = re.findall(r"\[(.*?)\]", s)
    list_of_nums = []
    for new in newstr:
        try:
            list_of_nums.append(int(new))
        except:
            print("Not a num")
            continue
    return list_of_nums

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
