import cv2

img = cv2.imread('dog.png')
gray = cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('dog Image',img)
cv2.imshow('gray img',gray)
# img = cv2.resize(img,(1,1))

cv2.waitKey(0)
#cv2.waitKey(250)
cv2.destroyAllWindows()
