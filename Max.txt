import numpy as np,cv2 as cv

def max (my_image,filtersize=3):
    
    rows,columns=np.shape(my_image)
    padding=int(np.floor(filtersize/2))
    max_img = np.zeros((int (rows-padding),int (columns-padding)),dtype=np.uint8)
    
    for i in range (padding,rows-padding):
        for j in range (padding,columns-padding):

            my_box=my_image[i-padding:i+padding+1,j-padding:j+padding+1]
            my_array=np.ravel(my_box)
            np.sort(my_array)
            max_img[i,j]=np.max(my_array)

    return max_img
                    

my_image1=np.array(cv.imread('Fig01.tif',0))
my_image2=np.array(cv.imread('Fig02.tif',0))

max1 = max(my_image1, 15)
max2 = max(my_image2, 31)

cv.imshow('Max Image 1', max1)
cv.imshow('Max Image 2', max2)

cv.waitKey(10000)
cv.destroyAllWindows()

cv.imwrite('Max Image 1.png',max1)
cv.imwrite('Max Image 2.png',max2)
