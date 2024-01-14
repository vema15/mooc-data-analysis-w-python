#!/usr/bin/env python3
import math


def main():
    while True:
        user_input = input("Choose a shape (triangle, rectangle, circle):\n")
        if user_input == 'triangle':
            tri_base = int(input("Give base of the triangle: "))
            tri_height = int(input("Give height of the triangle: "))
            print(f"The area is {0.5 * (tri_base * tri_height):.6f}")
        elif user_input == 'rectangle':
            rect_width = int(input("Give width of rectangle: "))
            rect_height = int(input("Give height of rectangle: "))
            print(f"The area is {(rect_width * rect_height):.6f}")
        elif user_input == 'circle':
            cir_rad = int(input("Give radius of the circle: "))
            print(f"The area is {(math.pi * (cir_rad**2)):.6f}")
        elif user_input == '':
            break
        else:
            print("Unknown shape!")
if __name__ == "__main__":
    main()
