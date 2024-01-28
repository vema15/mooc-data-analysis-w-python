#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    pic2 = img.copy()
    pic2 = np.sum(pic2[0:,0:]*[0.2126, 0.7152, 0.0722], axis=2)
    plt.gray()
    return pic2

def to_red(img):
    pic2 = img.copy()
    pic2 = pic2[0:,0:]* [1, 0, 0]
    return pic2
 
def to_green(img):
    pic2 = img.copy()
    pic2 = pic2[0:,0:]* [0, 1, 0]
    return pic2
 
def to_blue(img):
    pic2 = img.copy()
    pic2 = pic2[0:,0:]* [0, 0, 1]
    return pic2

def main():
    img = plt.imread("src/painting.png")
    fig, ax = plt.subplots(4, 1)
    ax[0].imshow(to_red(img))
    ax[1].imshow(to_green(img))
    ax[2].imshow(to_blue(img))
    ax[3].imshow(to_grayscale(img))
    plt.imshow(to_grayscale(img))
    plt.show()

if __name__ == "__main__":
    main()
