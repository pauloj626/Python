import cv2
import numpy as np 
from class_process import *

img = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)

ImP = ImageProcess(img)

ImP.cisalhamento(0, 20)

ImP.show('cis') 