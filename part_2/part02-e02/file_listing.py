#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    info_list = []
    with open(filename, "r") as listing_file:
        for line in listing_file:
            line = line.strip("\n")
            all_match = re.search("-all", line)
            start_ind = all_match.end()+1
            stripped_list = line[start_ind:].lstrip().split(" ")
            if "" in stripped_list:
                stripped_list.remove("")
            append_tuple = []
            for i in range(len(stripped_list)):
                if i == 3:
                    for j in stripped_list[i].split(":"):
                        append_tuple.append(int(j))
                else:
                    try:
                        append_tuple.append(int(stripped_list[i]))
                    except:
                        append_tuple.append(stripped_list[i])
            info_list.append(tuple(append_tuple))
    return info_list

def main():
    file_listing()

if __name__ == "__main__":
    main()
