#!/usr/bin/env python3
import re
def file_extensions(filename):
    file_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip("\n")
            file_list.append(line)
    existing_types = []
    no_type_list = []
    file_type_dict = {}
    for i in file_list:
        if "." in i:
            file_type = i[(len(i) - re.search('\.', "".join(reversed(i))).start()):]
            if file_type not in existing_types:
                file_type_dict[file_type] = []
                for j in file_list:
                    if file_type in j:
                        file_type_dict[file_type].append(j)
            existing_types.append(file_type)
        else:
            no_type_list.append(i)
    return (no_type_list, file_type_dict)

def main():
    file = 'src/filenames.txt'
    file_list = file_extensions(file)
    for index in range(len(file_list)):
        if index == 0:
            print(f'{len(file_list[index])} files with no extension')
        else:
            for key, value in sorted(file_list[index].items()):
                print(f'{key} {len(value)}')



if __name__ == "__main__":
    main()
