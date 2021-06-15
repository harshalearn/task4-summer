import cv2
SPACE=cv2.imread('SPACE.jpg')
GMARBLES=cv2.imread('GMARBLES.jpg')


rSPACE=cv2.rectangle(SPACE,(110,100),(380,400), (0,100,255), 3)
cv2.imshow('rSPACE', rSPACE)
cv2.waitKey()
cv2.destroyAllWindows()


rGMARBLES=cv2.rectangle(GMARBLES,(310,100),(580,400), (0,100,255), 3)
cv2.imshow('rGMARBLES', rGMARBLES)
cv2.waitKey()
cv2.destroyAllWindows()


cSPACE=SPACE[100:400,110:380]
cv2.imwrite('cSPACE.jpg',cSPACE)
cv2.imshow('cSPACE', cSPACE)
cv2.waitKey()
cv2.destroyAllWindows()


cGMARBLES=GMARBLES[100:400,310:580]
cv2.imwrite('cGMARBLES.jpg',cGMARBLES)
cv2.imshow('cGMARBLES', cGMARBLES)
cv2.waitKey()
cv2.destroyAllWindows()

sGMARBLES=GMARBLES
cv2.imshow('sGMARBLES', sGMARBLES)
cv2.waitKey()
cv2.destroyAllWindows()


sGMARBLES[100:400,310:580]=cSPACE
cv2.imshow('swGMARBLES', sGMARBLES)
cv2.waitKey()
cv2.destroyAllWindows()


sGMARBLES[100:400,310:580]=cSPACE
cv2.imshow('swGMARBLES', sGMARBLES)
cv2.waitKey()
cv2.destroyAllWindows()

sSPACE=SPACE
cv2.imshow('sSPACE', sSPACE)
cv2.waitKey()
cv2.destroyAllWindows()


cGMARBLES=cv2.imread('cGMARBLES.jpg')
sSPACE[100:400,110:380]=cGMARBLES
cv2.imwrite('sSPACE.jpg',sSPACE)
sSPACE=cv2.imread('sSPACE.jpg')
cv2.imshow('srSPACE', sSPACE)
cv2.waitKey()
cv2.destroyAllWindows()