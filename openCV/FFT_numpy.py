import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('graywoman.jpg', cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)

magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('Input image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude spectrum')
plt.xticks([])
plt.yticks([])

plt.show()