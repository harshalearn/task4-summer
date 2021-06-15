import cv2
import numpy

hphoto=numpy.empty(shape=(680,1277,3))
i=0
bl=0
gr=0
re=255
for gr in range(256):
    hphoto[:,i]=[bl,gr,re]
    i=i+1
for re in range(1,256):
    r=255-r
    hphoto[:,i]=[bl,gr,re]
    i=i+1
for bl in range(1,256):
    hphoto[:,i]=[bl,gr,re]
    i=i+1
for gr in range(1,256):
    gr=255-gr
    hphoto[:,i]=[bl,gr,re]
    i=i+1
for re in range(1,256):
    hphoto[:,i]=[bl,gr,re]
    i=i+1
for bl in range(1,256):
    bl=255-bl
    hphoto[:,i]=[bl,gr,re]


cv2.imwrite('hphoto.jpg',hphoto)
hphoto=cv2.imread('hphoto.jpg')

cv2.imshow('Hello', hphoto)
cv2.waitKey()
cv2.destroyAllWindows()