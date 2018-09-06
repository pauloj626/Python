import cv2
import numpy as np 
import matplotlib.pyplot as plt 

#IMREAD_GRAYSCALE
#IMREAD_COLOR
#IMREAD_UNCHANGED
img = cv2.imread('teste.jpg', cv2.IMREAD_GRAYSCALE)

#Open image with cv2

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#save the image
cv2.imwrite('graywoman.jpg', img)


'''
Open image with matplotlip
'''
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.plot([0,200], [10, 202], 'c', linewidth = 5)
#plt.show()