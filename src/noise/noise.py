#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import sys
import cv2
from pathlib import Path

def circle_noise(img, sigma):
    
    row,col,ch= img.shape
    mean = 0
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    x = row / 2
    y = col / 2
    rate = 0.6

    for i in range(row):
        for j in range(col):
            if (i-x)**2+(j-y)**2 < ((x*rate)**2 + (y*rate)**2):
                gauss[i][j] = 0
    
    cv2.imwrite("./result/" + str(sigma) + "_noise.jpg", gauss)

    gauss_img = img + gauss

    return gauss_img

def main():

    args = sys.argv
    brank = ""
    name = args[1].replace(".jpg", brank)
    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    image = str(dataset_path) + "/" + args[1]
    img = cv2.imread(image)
    sigma = int(args[2])

    th  = circle_noise(img, sigma)
    
    cv2.imwrite("./result/" + name + "_" + str(sigma)+ "_circle_noise.jpg", th)

if __name__ == "__main__":
    main()


