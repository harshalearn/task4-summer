import cv2 
import numpy


SPACE=cv2.imread('SPACE.jpg')
cv2.imshow('SPACE',SPACE)
cv2.waitKey()
cv2.destroyAllWindows()


GMARBLES=cv2.imread('GMARBLES.jpg')
cv2.imshow('GMARBLES',GMARBLES)
cv2.waitKey()
cv2.destroyAllWindows()


photo=numpy.empty(shape=(780,1277,3))
photo[:,:]=[133,133,133]
GMARBLES=cv2.imread('GMARBLES.jpg')
photo[0:434,572:1277]=GMARBLES
photo[60:712,450:811]=SPACE
cv2.imwrite('collage.jpg',photo)
collage=cv2.imread('collage.jpg')
cv2.imshow('collage',collage)
cv2.waitKey()
cv2.destroyAllWindows()