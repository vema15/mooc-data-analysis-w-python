#!/usr/bin/env python3

import sys
import functools
import math
import re

def summary(filename):
    with open(filename, 'r') as file:
        sum = 0
        count = 0
        list_of_nums = []
        for line in file:
            try:
                line = float(line.strip("\n"))
            except:
                continue
            sum += line
            count += 1
            list_of_nums.append(line)
        if count == 0:
            avg = 0
            standev = 0
        else:
            avg = sum/count
            dev_nums = [((i - avg)**2) for i in list_of_nums]
            standev_sum = 0
            for i in dev_nums:
                standev_sum += i
            standev = math.sqrt(standev_sum/(count-1))
        return (float(sum), float(avg), float(standev))
            


def main():
    #summary("/Users/ethanacevedo/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2023-2024/part02-e05_summary/src/example.txt")
    orig_arv = sys.argv
    for i in sys.argv[1:]:
        summary_output = summary(i)
        print(f"File: {i} Sum: {summary_output[0]:.6f} Average: {summary_output[1]:.6f} Stddev: {summary_output[2]:.6f}")

    
    #for i in range(8):
    #    if i == 0:
    #        continue
    #    if i == 1:
    #        file = "src/example.txt"
    #    elif i > 1:
    #        file = f"src/example{i}.txt"
    #    curr_summary = summary(file)
    #    print(f"File: file{str(i)} Sum: {curr_summary[0]:.6f} Average: {curr_summary[1]:.6f} Stddev: {curr_summary[2]:.6f}")
    


if __name__ == "__main__":
    main()
