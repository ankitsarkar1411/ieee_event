import cv2
img=cv2.imread("cat.jpg")
gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray_img.ndim)
net,binary_img= cv2.threshold(gray_img,150,255,cv2.THRESH_BINARY)
print(net,binary_img)
cv2.imshow("binary_image",binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
