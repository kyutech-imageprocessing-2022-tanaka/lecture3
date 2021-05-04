import cv2

img = cv2.imread('mandrill.jpg')

h, w, c = img.shape

mat = cv2.getRotationMatrix2D( (w/2, h/4), 30, 0.5)

img2 = cv2.warpAffine(img, mat, (w, h))

cv2.imshow("Image", img)
cv2.imshow("Image1",img2)

key = cv2.waitKey(0)

cv2.destroyAllWindows()
