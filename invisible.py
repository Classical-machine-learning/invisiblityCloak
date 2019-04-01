import cv2
import time
import numpy as np
import pickle

with open('range.pickle','rb') as f:
    t = pickle.load(f)

lower_red = np.array([t[0],t[1],t[2]])
upper_red = np.array([t[3],t[4],t[5]])


cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0



#initial capture

for i in range(50):
    ret,background = cap.read()

background = np.flip(background,axis = 1)


while True:
    ret,img = cap.read()
    img = np.flip(img,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv,lower_red,upper_red)

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img,img,mask=mask2)

    res2 = cv2.bitwise_and(background,background,mask=mask1)

    final = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("Evanesco",final)
    cv2.waitKey(1)
