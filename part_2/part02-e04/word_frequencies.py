#!/usr/bin/env python3
import re

def word_frequencies(filename):
    count_dict = {}
    readable_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = re.sub(r"[^\w\s]", "", line)
            line = re.sub(r"_", "", line)
            line = re.sub(r"\n", '', line)
            for word in line.split(" "):
                readable_list.append(word)
    for index in readable_list:
        if index not in count_dict:
            count_dict[index] = readable_list.count(index)
    print(len(count_dict))
    return count_dict


def main():
    word_frequencies("/Users/ethanacevedo/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2023-2024/part02-e04_word_frequencies/src/alice.txt")

if __name__ == "__main__":
    main()
