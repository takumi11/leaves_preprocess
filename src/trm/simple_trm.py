#! /use/bin/env python
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import numpy as np
from pathlib import Path
from glob import glob
from tqdm import tqdm

def first_trm(img, height, width):

    if width >= height:
        size = height
    else:
        size = width

    half_size = size // 2
    h = height // 2
    w = width // 2

    first_trm = img[h -half_size : h + half_size, w - half_size : w + half_size]

    return first_trm

def re_size(img, size):

    size = (size, size)
    resize = cv2.resize(img, size)

    return resize

def trm(img, height, width, trmsize):

    temp = trmsize // 2
    h = height // 2
    w = width // 2

    trm = img[h-temp : h+temp, w-temp : w+temp]

    return trm


def make_data(data, method, resize, scale, trmsize, brank):

    img =cv2.imread(data)
    height, width, channels = img.shape
    data_number = data.replace(".jpg", brank)

    if not height == width:
        img = first_trm(img, height, width)
        cv2.imwrite(data_number + "_first_trm" + ".jpg", img)

    img_resize = re_size(img, resize)
    cv2.imwrite(data_number + "_resize" +".jpg", img_resize)
    reheight, rewidth, rechannels = img_resize.shape
    img_out = trm(img_resize, reheight, rewidth, trmsize)
    cv2.imwrite(data_number + "_out" + ".jpg", img_out)


def main():

    brank = ""
    method = "trm"

    resize = 64
    scale = 1.0
    trmsize = 32
    image1 = "000025.jpg"
    image2 = "000032.jpg"

    make_data(image1, method, resize, scale, trmsize, brank)
    make_data(image2, method, resize, scale, trmsize, brank)


if __name__ == "__main__":
    main()

