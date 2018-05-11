#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from glob import glob
from pathlib import Path


def main():

    path = str(Path(__file__).resolve().parent) + "/"
    brank = ""
    method = 'mask'

    for image in glob(path + "*.jpg"):
        img = cv2.imread(image, 1)
        mask = cv2.imread("mask_cir02.jpg", 0)
        img_path = image.replace(path, brank)
        img_masked = cv2.bitwise_and(img, img, mask = mask)

        cv2.imwrite(path + method + "/" + img_path, img_masked)

if __name__ == '__main__':
    main()

