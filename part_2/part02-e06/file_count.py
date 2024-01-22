#!/usr/bin/env python3

import sys
import re

def file_count(filename):
    with open(filename, 'r') as file:
        count_dict = {
            'line_ct': 0,
            'word_ct': 0,
            'char_ct': 0
        }
        for line in file:
            count_dict['line_ct'] += 1
            count_dict['char_ct'] += len(line)
            line = line.strip("\n")
            split_line = line.split(" ")
            if len(split_line) == 1 and split_line[0] == "":
                continue
            else:
                count_dict['word_ct'] += len(split_line)
            
        return (count_dict['line_ct'], count_dict['word_ct'], count_dict['char_ct'])

def main():
    orig_argv = sys.argv
    for i in orig_argv[1:]:
        file_name = i
        count_info = file_count(file_name)
        print(f'{count_info[0]}\t{count_info[1]}\t{count_info[2]}\t{file_name}')
   

if __name__ == "__main__":
    main()
