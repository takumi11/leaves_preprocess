#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2
import sys
from pathlib import Path

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

    gamma = 0.8
    imax = gray.max()
    th1 = imax * (gray / imax) ** (1 / gamma)
    cv2.imwrite("./result/" + name + "_gamma.jpg", th1)

if __name__ == "__main__":
    main()

