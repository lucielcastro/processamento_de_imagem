import cv2
img = cv2.imread('aula2/logo-if.jpg')

roi=img[0:150,0:150]
cv2.imshow('Logo IF',roi)

cv2.waitKey(0)
cv2.destroyAllWindows()