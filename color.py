import cv2 
import numpy as np  
cap = cv2.imread('2000_final.jpeg')
cap = cv2.resize(cap, (340,480))
shap=cap.shape
red=np.zeros([shap[0],shap[1]])
green=np.zeros([shap[0],shap[1]])
blue=np.zeros([shap[0],shap[1]])
for x in range (shap[0]):
    for y in range(shap[1]):
        red[x][y] = cap[x][y][0]
        green[x][y] = cap[x][y][1]
        blue[x][y] = cap[x][y][2]
print(np.mean(red))
print(np.mean(green))
print(np.mean(blue))