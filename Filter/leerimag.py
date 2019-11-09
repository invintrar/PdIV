import cv2

img = cv2.imread("lena.bmp",0)

cv2.imshow("First", img)

# Wait for keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()