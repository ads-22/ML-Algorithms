import cv2

img = cv2.imread('simon.jpg')

cv2.imshow('Bird Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
