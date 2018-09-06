import numpy as np 
import cv2

img = cv2.imread('teste.jpg', cv2.IMREAD_COLOR)

#cv2.line(where, begin, finish, color, line_width)
cv2.line(img, (0,0), (400, 300), (255, 255, 255), 5)

#cv2.line(where, top_left, botton_rigth, color, line_width)
cv2.rectangle(img, (0, 0), (400, 450), (0, 0, 0), 5)

#cv2.circle(where, center, radius, color, line_width) obs: line_width = -1 -> fill object
cv2.circle(img, (200, 225), 200, (255, 0, 0), -1)

pts = np.array([[0, 10], [20, 78], [5, 304], [123, 32]], np.int32)
#pts = pts.reshape((-1, 1, 2))

#cv2.polylines(where, points, "conect the final point with the first point", color, line_width)
cv2.polylines(img, [pts], True, (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0, 133), font, 0.5, (200, 202, 2), 2, cv2.CV_AA)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()