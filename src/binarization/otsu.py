#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2
import sys
from pathlib import Path

def threshold_otsu(gray, img_shape, min_val=0, max_val=255):

    hist = [np.sum(gray == i) for i in range(256)]
    print(img_shape)
    s_max = (0, -10)

    for th in range(256):
        n1 = sum(hist[:th])
        n2 = sum(hist[th:])

        if n1 == 0:mu1 = 0
        else:mu1 = sum([i * hist[i] for i in range(0, th)]) / n1
        if n2 == 0:mu2 = 0
        else:mu2 = sum([i * hist[i] for i in range(th, 256)]) / n2

        s = n1 * n2 * (mu1 - mu2) ** 2

        if s > s_max[1]:
            s_max = (th, s)

    t = s_max[0]
    print(t)
    for i in range(img_shape[0]-1):
        for j in range(img_shape[1]-1):
            if gray[i][j] >= t:
                gray[i][j] = max_val
            elif gray[i][j] < t:
                gray[i][j] = min_val

    return gray

def main():

    args = sys.argv
    brank = ""
    name = args[1].replace(".jpg", brank)
    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    image = str(dataset_path) + "/" + args[1]
    img = cv2.imread(image)
    img_shape = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    th1 = threshold_otsu(gray, img_shape)

    cv2.imwrite("./result/" + name + "_otsu.jpg", th1)

if __name__ == "__main__":
    main()

