#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import cv2
from pathlib import Path


def fft(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    return magnitude_spectrum

#def noise(img):
 
def main():

    args = sys.argv
    brank = ""
    name = args[1].replace(".jpg", brank)
    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    image = str(dataset_path) + "/" + args[1]
    img = cv2.imread(image)

    th = fft(img)

    cv2.imwrite("./result/" + name + "_fft.jpg", th)

if __name__ == "__main__":
    main()

