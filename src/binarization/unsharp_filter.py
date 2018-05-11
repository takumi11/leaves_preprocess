#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from PIL import Image, ImageDraw
from pathlib import Path

def unsharp_filter(img, w, h, k):

    pixcels = np.array([[img.getpixel((x,y)) for x in range(w)] for y in range(h)])
    filtered_img = Image.new('RGB', (w, h))
    cr = 1 + 8 * k / 9
    ar = - k / 9

    for x in range(w):
        for y in range(h):
            if x == 0 or x == w - 1 or y == h - 1:
                filtered_pixcel = pixcels[y][x]
            else:
                filtered_pixcel =   ar * pixcels[y - 1][x - 1] + ar * pixcels[y - 1][x]\
                                  + ar * pixcels[y - 1][x + 1]+ ar * pixcels[y][x - 1]\
                                  + cr * pixcels[y][x] + ar * pixcels[y][x - 1]\
                                  + ar * pixcels[y + 1][x - 1]\
                                  + ar * pixcels[y + 1][x] + ar * pixcels[y + 1][x + 1]

            filtered_img.putpixel((x,y), (tuple(list(map(int, filtered_pixcel)))))

    return filtered_img

def main():
    args = sys.argv
    brank = ""
    k = int(args[2])
    name = args[1].replace(".jpg", brank)
    current = Path()
    dataset_path = current.resolve().parent.parent/'data'/'treated'
    image = str(dataset_path) + "/" + args[1]
    img = Image.open(image).convert("RGB")
    w, h = img.size

    unsharp_img = unsharp_filter(img, w, h, k)
    unsharp_img.save("./result/" + name + "_" + str(k) + "_unsharp_filter.jpg")

if __name__ == '__main__':
    main()

