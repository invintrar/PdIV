import cv2


background = cv2.imread('image/c.jpg')
overlay = cv2.imread('image/yo4.png')

rows,cols,channels = overlay.shape

overlay = cv2.addWeighted(background[250:250+rows, 0:0+cols], 0.1, overlay,0.9,0)

background[1900:1900+rows, 1500:1500+cols] = overlay

cv2.imwrite('conbined.png', background)

cv2.waitKey(0)

