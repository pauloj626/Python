import cv2
import numpy as np 
import matplotlib.pyplot as plt

def mostraImg(*imgs):
	for img in imgs:
		cv2.imshow(img[1], img[0])
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':

	imgGray  = cv2.imread('teste.jpg', cv2.IMREAD_GRAYSCALE)
	imgColor = cv2.imread('fig_lista3_1.png', cv2.IMREAD_COLOR) 

	#mostraImg((imgGray, 'gray'), (imgColor, 'color'))

	#hist = cv2.calcHist([imgGray],[0],None,[256],[0,256])
	#hist,bins = np.histogram(imgGray.ravel(),256,[0,256])
	#hist = np.bincount(img.ravel(),minlength=256)

	plt.hist(imgGray.ravel(),256,[0,256])
	#plt.imshow(imgGray)
	plt.show()
	'''
	color = ('b','g','r')
	for i,col in enumerate(color):
		histr = cv2.calcHist([imgColor],[i],None,[256],[0,256])
		plt.plot(histr,color = col)
		plt.xlim([0,256])
	plt.show()
	'''