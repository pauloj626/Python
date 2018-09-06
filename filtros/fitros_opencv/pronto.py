import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
 
#kernel = np.ones((5,5),np.float32)/25
#kernel = np.asarray([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
#kernel = np.asarray([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#kernel = np.asarray([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
kernel = np.ones((17,17),np.float32)/(17**2)
dst = cv2.filter2D(img,-1,kernel)

print(dst)
print('min, max = ', dst.min(), dst.max())

cv2.imwrite('17x17.png', dst)

plt.subplot(121),plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.subplot(122),plt.imshow(dst, cmap = 'gray'),plt.title('Averaging')
plt.show()