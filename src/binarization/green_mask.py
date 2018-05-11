#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    
    #green_min = np.array([0,140, 0], np.uint8)
    #green_max = np.array([255, 255, 255], np.uint8)

    green_min = np.array([40, 50, 50])
    green_max = np.array([80, 255, 255])

    args = sys.argv
    brank = ""
    name = args[1].replace(".jpg", brank)
    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    image = str(dataset_path) + "/" + args[1]
    img = cv2.imread(image)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    plt.imshow(cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB))
    plt.show("img")

    #mask_green = cv2.inRange(img, green_min, green_max)
    mask_green = cv2.inRange(img_hsv, green_min, green_max)
    plt.imshow(mask_green)
    plt.show("mask_green")

    mask = cv2.bitwise_not(mask_green)
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    plt.imshow(mask_rgb)
    plt.show("mask")

    reverse_mask = cv2.bitwise_not(mask_rgb)
    plt.imshow(reverse_mask)
    plt.show("mask")

    cv2.imwrite("./result/" + name + "_green_mask.jpg", reverse_mask)

if __name__ == "__main__":
    main()

