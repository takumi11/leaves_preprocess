#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
from pathlib import Path

def main():
    
    args = sys.argv
    brank = ""
    name = args[1].replace(".jpg", brank)
    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    image = str(dataset_path) + "/" + args[1]
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    canny_img = cv2.Canny(gray, 80, 200)

    cv2.imwrite("./result/" + name + "_canny.jpg", canny_img)


if __name__ == "__main__":
    main()

