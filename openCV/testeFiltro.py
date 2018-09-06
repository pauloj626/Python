import matplotlib.pyplot as plt
import numpy as np 
import cv2

def getImage(nome):
	return cv2.imread(nome, cv2.IMREAD_COLOR)

def filterBlue(img):
	for line in img:
		for pix in line:
			pix[0] = 0

def filterGreen(img):
	for line in img:
		for pix in line:
			pix[1] = 0

def filterRed(img):
	for line in img:
		for pix in line:
			pix[2] = 0

def showImage_cv2(img):
	cv2.imshow('image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

img = getImage('python.png')

filterBlue(img)
#filterGreen(img)
filterRed(img)

print(img)

showImage_cv2(img)