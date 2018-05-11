#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from glob import glob
from pathlib import Path

def main():

    path = str(Path(__file__).resolve().parent) + "/"

    img = x=np.zeros((224, 224))
    _x=x+123.68
    y=np.zeros((224, 224))
    _y=y+116.779
    z=np.zeros((224, 224))
    _z=z+103.939
    imagenet_mean = np.array((_x, _y, _z))
    imagenet_mean = imagenet_mean.transpose(2,1,0)
    brank = ""
    cv2.imwrite("imagenet_mean.png", imagenet_mean)

    for image in glob(path + "*.png"):
        img = cv2.imread(image)
        height, width, channels = img.shape
        img_path = image.replace(path, brank)

        img = img - imagenet_mean

        cv2.imwrite(path + "mean/" + img_path, img)



if __name__ == '__main__':
    main()

