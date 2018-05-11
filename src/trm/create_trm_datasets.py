#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import numpy as np
from glob import glob
from tqdm import tqdm
import shutil
import os
import math

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

def main():

    min_angle = 0
    max_angle = 360
    step_angle = 10
    scale = 1.0
    resize = 64
    trmsize = 32
    brank = ""

    original_path = "/Users/saikawatakumi/Desktop/dir/program_sample/python_code/playing_code/opencv_playing/leaves/trm/original_01/"
    save_train_path = "/Users/saikawatakumi/Desktop/dir/program_sample/data_set/sample_datasets02/train/"
    save_test_path = "/Users/saikawatakumi/Desktop/dir/program_sample/data_set/sample_datasets02/test/"

    four_fold = [0, 1, 2, 3]
    flip_switch = [0, 1]

### make test datasets.......
#    print("creating test datasets now")
#    for num in tqdm(four_fold):
#        current_path = original_path + str(num) + "/"
#        for path in tqdm(glob(current_path + "*.jpg")):
#            data_name = path.replace(current_path, brank)
#            img = cv2.imread(path)
#            out_img = make_test(img, resize, trmsize)
#            cv2.imwrite(save_test_path + str(num) + "/" + data_name, out_img)
#    print("finish !")

### make train datasets.......
    print("creating train datasets now")
    for num in tqdm(four_fold):
        current_path = original_path + str(num) + "/"
        for path in tqdm(glob(current_path + "*.jpg")):
            for flip_num in flip_switch:
                for angle in range(min_angle, max_angle, step_angle):
                    data_name = path.replace(current_path, brank)
                    num_name = data_name.replace(".jpg", brank)
                    data_size = len(str(angle))
                    if data_size == 1:
                        angle_name = "00" + str(angle)
                    elif data_size == 2:
                        angle_name = "0" + str(angle)
                    else:
                        angle_name = str(angle)
                    img = cv2.imread(path)
                    out_img = make_train(img, angle, flip_num, scale, resize, trmsize)
                    cv2.imwrite(save_train_path  + str(num) + "/" + num_name + angle_name + str(flip_num) + ".jpg", out_img)
    print("finish !")

if __name__ == '__main__':
    main()
