#!/usr/bin/env python3

def interleave(*lists):
    zipped_list = list(zip(*lists))
    unpacked_list = []
    def unpack_zip(zipped_list):
        for i in zipped_list:
            if type(i) == tuple:
                unpack_zip(i)
            else:
                unpacked_list.append(i)
    unpack_zip(zipped_list)
    return unpacked_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
