import numpy as np
import cv2 as cv

def laplacian(img,mask):
    return cv.filter2D(img,-1,mask)

def normalize(img):
    img_1=np.array(img,dtype=np.uint8)
    rows,columns = np.shape(img)
    img_min = np.min(img)
    img_max = np.max(img)
    for i in range(rows):
        for j in range(columns):
            img_1[i,j] = 255*((img[i,j] - img_min)/(img_max-img_min))
    return img_1
    

mask=np.array(((-1,-1,-1),
               ( 1, 8,-1),
               (-1,-1,-1)),dtype=np.float32)

img=np.array(cv.imread('Fig03.tif'),dtype=np.float32)

filtered_img = laplacian(img, mask)

final_img = filtered_img + img

final_img = normalize(final_img)

cv.imshow('Orginal Image', img)
cv.imshow('Laplacian Filtered Image',filtered_img)
cv.imshow('Final Image', final_img)
cv.waitKey(10000)
cv.destroyAllWindows()
