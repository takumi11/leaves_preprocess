#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from pathlib import Path

def main():

    #image = '000001.jpg'
    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    image_path = str(dataset_path) + "/"
    brank = ""
    method = 'edge'

    for image in glob(image_path + '*.jpg'):
        img = cv2.imread(image,0)
        edge_img = cv2.Canny(img, 100, 200)
        img_path = image.replace(image_path, brank)
        #cv2.imshow('edge', edge_img)
        cv2.imwrite("./result/" + method + img_path, edge_img)
    #plt.colorbar()
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
