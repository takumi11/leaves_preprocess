#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys
import seaborn as sns
from matplotlib import pyplot as plt
from pathlib import Path

def rgb_hist(rgb_img):
    
    sns.set()
    sns.set_style(style='ticks')
    fig = plt.figure(figsize=[15,4])
    ax1 = fig.add_subplot(1,2,1)
    sns.set_style(style='whitegrid')
    ax2 = fig.add_subplot(1,2,2)

    ax2 = fig.add_subplot(1,2,2)

    color=['r','g','b']

    for (i,col) in enumerate(color): # 各チャンネルのhist
        # cv2.calcHist([img], [channel], mask_img, [binsize], ranges)
        hist = cv2.calcHist([rgb_img], [i], None, [256], [0,256])
        # グラフの形が偏りすぎるので √ をとってみる
        hist = np.sqrt(hist)
        ax2.plot(hist,color=col)
        ax2.set_xlim([0,256])

    plt.show()

def main():

    args = sys.argv
    brank = ""
    name = args[1].replace(".jpg", brank)
    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    image = str(dataset_path) + "/" + args[1]
    img = cv2.imread(image)

    rgb_hist(img)

if __name__ == "__main__":
    main()

