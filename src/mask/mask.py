#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from glob import glob
from pathlib import Path


def main():

    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    path = str(dataset_path) + "/"
    brank = ""
    method = 'mask'
    rate= 0.6
    x = 112
    y = 112

    for image in glob(path + "*.jpg"):
        img = cv2.imread(image)
        height, width, channels = img.shape
        #mask = cv2.imread("mask_cir02.jpg", 0)
        img_path = image.replace(path, brank)
        #img_masked = cv2.bitwise_and(img, img, mask = mask)

        for i in range(height):
            for j in range(width):
                if (i-x)**2+(j-y)**2 > ((x*rate)**2 + (y*rate)**2) :
                    img[i][j] = 0

        cv2.imwrite("./result/" + img_path, img)

if __name__ == '__main__':
    main()

