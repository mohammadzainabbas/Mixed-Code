import numpy as np,cv2 as cv

def min (my_image,filtersize=3):
    
    rows,columns=np.shape(my_image)
    padding=int(np.floor(filtersize/2))
    min_img = np.zeros((int (rows-padding),int (columns-padding)),dtype=np.uint8)
    
    for i in range (padding,rows-padding):
        for j in range (padding,columns-padding):

            my_box=my_image[i-padding:i+padding+1,j-padding:j+padding+1]
            my_array=np.ravel(my_box)
            np.sort(my_array)
            min_img[i,j]=np.min(my_array)

    return min_img
                    

my_image1=np.array(cv.imread('Fig01.tif',0))
my_image2=np.array(cv.imread('Fig02.tif',0))

min1 = min(my_image1, 15)
min2 = min(my_image2, 31)

cv.imshow('Min Image 1', min1)
cv.imshow('Min Image 2', min2)

cv.waitKey(10000)
cv.destroyAllWindows()

cv.imwrite('Min Image 1.png',min1)
cv.imwrite('Min Image 2.png',min2)