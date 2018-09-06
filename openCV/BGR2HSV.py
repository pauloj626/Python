import numpy as np 
import cv2

def hsvFilter(hue_min, hue_max, sat_min, sat_max, val_min, val_max, img):
	for i in img:
		for pix in i:
			if(hue_min <= pix[0] <= hue_max and sat_min <= pix[1] <= sat_max and val_min <= pix[2] <= val_max):
				pix[0] = 0
				pix[1] = 0
				pix[2] = 0


img = cv2.imread('image/logopy.png', cv2.IMREAD_COLOR)

imhsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsvFilter(24, 28, 200, 260, 200, 260, imhsv)

cv2.imshow('imgFil', imhsv)
#cv2.imshow('original', img)

cv2.waitKey(0)

cv2.destroyAllWindows()