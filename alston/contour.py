import cv2
import numpy as np
imaage_var = "Image-003.jpg"
img = cv2.imread(imaage_var,0)
(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU )
cv2.imshow("im_bw",im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh = cv2.threshold(im_bw,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

im = cv2.imread(imaage_var,cv2.IMREAD_COLOR)
i=0

for cnt in contours:

    x,y,w,h = cv2.boundingRect(cnt)
    crop_img = im[y:y+h, x:x+w] 
    cv2.imwrite("result/cropped-"+str(i)+".png", crop_img)
    i = i+1
    
cv2.imshow("",im)
cv2.imwrite('result/grayimage.png',im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
