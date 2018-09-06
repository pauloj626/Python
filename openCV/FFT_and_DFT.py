import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('graywoman.jpg', cv2.IMREAD_GRAYSCALE)

########FFT############
f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)

img_FFT = 20*np.log(np.abs(fshift))

#######DFT###########
rows, cols = img_FFT.shape
crow, ccol = rows/2, cols/2

fshift[crow-30:crow+30, ccol-30:ccol+30] = 0

f_ishift = np.fft.ifftshift(fshift)

img_DFT = np.fft.ifft2(f_ishift)

img_DFT = np.abs(img_DFT)


plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('Input image')
plt.xticks([])
plt.yticks([])
'''
plt.subplot(122)
plt.imshow(img_FFT, cmap = 'gray')
plt.title('image FFT')
plt.xticks([])
plt.yticks([])
'''
plt.subplot(122)
plt.imshow(img_DFT, cmap = 'gray')
plt.title('image DFT')
plt.xticks([])
plt.yticks([])

plt.show()