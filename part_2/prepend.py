#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, user_string_1):
        self.user_string_1 = user_string_1
    
    def write(self, user_string_2):
        print(f"{self.user_string_1}{user_string_2}")

def main():
    x = Prepend("+++ ")
    x.write("Hello")

if __name__ == "__main__":
    main()
