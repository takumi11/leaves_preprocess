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

def main():

    data_path = str(Path(__file__).resolve().parent) + "/trm/original/"
    save_path = str(Path(__file__).resolve().parent) + "/trm/new_trm1/"
    print(data_path)
    print(save_path)
    brank = ""
    method = "trm"

    resize = 316
    scale = 1.0
    trmsize = 224

    for image in tqdm(glob(data_path + '*.jpg')):
        img = cv2.imread(image)
        file_name = image.replace(data_path, brank)
        #print(file_name)
        height, width, channels = img.shape
        if not height == width:
            img = first_trm(img, height, width)
        img_resize = re_size(img, resize)
        reheight, rewidth, rechannels = img_resize.shape
        img_out = trm(img_resize, reheight, rewidth, trmsize)
        #print(img_out.shape)
        #print("")
        #print(save_path + str(file_name))
        cv2.imwrite(save_path + str(file_name), img_out)

if __name__ == "__main__":
    main()

