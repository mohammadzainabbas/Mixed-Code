import numpy as np,cv2 as cv

def median (my_image,filtersize=3):
    
    rows,columns=np.shape(my_image)
    padding=int(np.floor(filtersize/2))
    median_img = np.zeros((int (rows-padding),int (columns-padding)),dtype=np.uint8)
    
    for i in range (padding,rows-padding):
        for j in range (padding,columns-padding):

            my_box=my_image[i-padding:i+padding+1,j-padding:j+padding+1]
            my_array=np.ravel(my_box)
            np.sort(my_array)
            median_img[i,j]=np.median(my_array)

    return median_img
                    

my_image1=np.array(cv.imread('Fig01.tif',0))
my_image2=np.array(cv.imread('Fig02.tif',0))

median1 = median(my_image1, 15)
median2 = median(my_image2, 31)

cv.imshow('Median Image 1', median1)
cv.imshow('Median Image 2', median2)

cv.waitKey(10000)
cv.destroyAllWindows()

cv.imwrite('Median Image 1.png',median1)
cv.imwrite('Median Image 2.png',median2)