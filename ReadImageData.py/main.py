# import packet
import cv2
img = cv2.imread("readimage.jpg")
print('image', img)
cv2.imshow("kenangan", img)

cv2.waitKey(0)
cv2.destroyAllWindows()