import cv2
import numpy as np

img = cv2.imread('mandrill.jpg')

h, w, c = img.shape

src_points = np.array([[0, 0], [0, h], [w, h], [w, 0]], dtype=np.float32)
dst_points = np.array([[50, 50], [30, 450], [400, 400], [300, 30]], dtype=np.float32)

mat = cv2.getPerspectiveTransform(src_points, dst_points)

img2 = cv2.warpPerspective(img, mat, (w, h))

cv2.imshow("Image", img)
cv2.imshow("Image1",img2)

key = cv2.waitKey(0)

cv2.destroyAllWindows()
