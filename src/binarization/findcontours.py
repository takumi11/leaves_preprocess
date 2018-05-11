#! /usr/bin/env python
# -*- cording: utf-8 -*-

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
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    image, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print("contours=",len(contours),  "hierarchy=",len(hierarchy))

    for i in contours:
        cv2.drawContours(image, contours[0], -1, (255, 0, 0), 3)

    cv2.imshow("img", image)
    cv2.imwrite("./result/" + name + "_findcontours.jpg", image)

if __name__ == '__main__':
    main()

