#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    
    with open(filename, "r") as color_file:
        clean_list = []
        for line in color_file:
            line = re.sub(r"\t", ' ', line)
            line = re.sub(r"\n", ' ', line)
            finding_useless = re.findall(" ", line)
            split_line = line.split(" ")
            test_line = [i for i in split_line if i]
            if len(test_line) > 4:
                test_line[3] = ' '.join(test_line[3:])
                del test_line[4:] 
            #for i in range(len(test_line)-1):
            #    test_line[i] = test_line[i]+'\t'
            #clean_list.append(test_line)
            clean_list.append(f'{test_line[0]}\t{test_line[1]}\t{test_line[2]}\t{test_line[3]}')
        return clean_list[1:] 

def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
