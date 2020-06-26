# -*- coding: utf-8 -*-
"""Currency Matcher.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/0B20zzeVCKx43Mk9Gamc5WEYxT1ZhYnIwT2w3Y3lyYThjTUZv
"""

from matplotlib import pyplot as plt
import cv2
import math
import numpy as np

max_val = 8
max_pt = -1
max_kp = 0

orb = cv2.ORB_create()

test_img = cv2.imread('100.jpeg')

# original=cv2.resize(test_img, None, fx=0.4, fy=0.4, interpolation = cv2.INTER_AREA)

# cv2.imshow('img',original)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

(kp1, des1) = orb.detectAndCompute(test_img, None)

training_set=['2000_1.jpeg','2000_1.jpg','2000_final.jpeg','100.jpg','100_1.jpg','100_2.jpg','200.jpeg','200_bachao.jpeg','500_rbi.jpeg','500_final.jpeg']

for i in range(0, len(training_set)):
    train_img = cv2.imread(training_set[i])
    (kp2, des2) = orb.detectAndCompute(train_img, None)
    bf = cv2.BFMatcher()
    all_matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for (m, n) in all_matches:
        if m.distance < 0.789 * n.distance:
            good.append([m])
    if len(good) > max_val:
        max_val = len(good)
        max_pt = i
        max_kp = kp2
    print(i, ' ', training_set[i], ' ', len(good))
if max_val >= 25 :
    print(training_set[max_pt])
    print('good matches ', max_val)
    train_img = cv2.imread(training_set[max_pt])
    img3 = cv2.drawMatchesKnn(test_img, kp1, train_img, max_kp, good, 4)
    note = str(training_set[max_pt]).split('.')
    note=note[0]
    print('\nDetected denomination: Rs. ', note)
    (plt.imshow(img3), plt.show())
else:
	print('Not a valid currency')

