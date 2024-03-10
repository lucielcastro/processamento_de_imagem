import cv2
# import 'logo'
img = cv2.imread('logo-if.jpg')

#TODO processar
# print(img)

cv2.imshow('Logo IF',img)

cv2.waitKey(0)
cv2.destroyAllWindows()