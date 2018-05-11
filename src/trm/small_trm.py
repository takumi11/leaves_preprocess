#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import numpy as np
from glob import glob
from tqdm import tqdm
import shutil
import os
from pathlib import Path

def affin(img, angle, scale):
    
    height, width, channels = img.shape
    size = (width, height)
    center = (size[0] // 2, size[1] // 2)

    rotation_matrix = cv2.getRotationMatrix2D(center, float(angle), scale)
    affin = cv2.warpAffine(img, rotation_matrix, size, flags=cv2.INTER_CUBIC)

    return affin

def first_trm(img):

    height, width, chanels = img.shape
    if width >= height:
        size = height
    else:
        size = width

    center = size // 2
    h = height // 2
    w = width // 2

    first_trm = img[h -center : h + center, w - center : w + center]

    return first_trm

def re_size(img, resize):

   size = (resize, resize)
   resize = cv2.resize(img, size)

   return resize

def trm(img, trmsize):
    
    height, width, chanels = img.shape
    temp = trmsize // 2
    h = height // 2
    w = width // 2

    trm = img[h-temp : h+temp, w-temp : w+temp]

    return trm

def flip(img):

    frip = cv2.flip(img, 1)

    return frip

def make_test(img, resize, trmsize):

    img = first_trm(img)
    img_resize = re_size(img, resize)
    img_out = trm(img_resize, trmsize)

    return img_out

def make_train(img, angle, flip_num, scale, resize, trmsize):

    img = first_trm(img)
    img_resize = re_size(img, resize)
    img_affin = affin(img_resize, angle, scale)
    img_trm = trm(img_affin, trmsize)
    if flip_num == 0:
        out_img = img_trm
    elif flip_num == 1:
        out_img = flip(img_trm)

    return out_img

def make_affin(img, angle, scale, resize, trmsize):

    img = first_trm(img)
    img_resize = re_size(img, resize)
    img_affin = affin(img_resize, angle, scale)

    return img_affin

def main():

    min_angle = 0
    max_angle = 360
    step_angle = 10
    scale = 1.0
    #resize = 64
    resize = 48
    trmsize = 32
    brank = ""

    original_path = str(Path(__file__).resolve().parent) + "/temp/"
    save_path01 = str(Path(__file__).resolve().parent) + "/temp02/"
    save_path02 = str(Path(__file__).resolve().parent) + "/temp03/"
    save_path03 = str(Path(__file__).resolve().parent) + "/affin/"

    flip_switch = [0, 1]

### make test datasets.......
    print("creating test datasets now")

    for path in tqdm(glob(original_path + "*.jpg")):
        data_name = path.replace(original_path, brank)
        img = cv2.imread(path)
        out_img = make_test(img, resize, trmsize)
        cv2.imwrite(save_path02 + data_name, out_img)
    print("finish !")

    print("make_affin")
    for path in tqdm(glob(original_path + "*.jpg")):
        for angle in tqdm(range(min_angle, max_angle, step_angle)):
            data_name = path.replace(original_path, brank)
            num_name = data_name.replace(".jpg", brank)
            img = cv2.imread(path)
            out_img = make_affin(img, angle, scale, resize, trmsize)
            cv2.imwrite(save_path03 + num_name + str(angle) + ".jpg", out_img)

### make train datasets.......
    print("creating train datasets now")

    for path in tqdm(glob(original_path + "*.jpg")):
        for flip_num in flip_switch:
            for angle in tqdm(range(min_angle, max_angle, step_angle)):
                data_name = path.replace(original_path, brank)
                num_name = data_name.replace(".jpg", brank)
                img = cv2.imread(path)
                out_img = make_train(img, angle, flip_num, scale, resize, trmsize)
                cv2.imwrite(save_path01 + num_name + str(angle) + str(flip_num) + ".jpg", out_img)
    print("finish !")

if __name__ == '__main__':
    main()
