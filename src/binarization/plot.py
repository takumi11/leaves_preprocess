#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

args = sys.argv
current = Path()
dataset_path = current.resolve().parent.parent/'data'/'treated'
image = str(dataset_path) + "/" + args[1]
img = cv2.imread(image, 0)

plt.imshow(img)
plt.colorbar()
plt.show()


