import numpy as np, cv2 as cv

def apply_filter (img,filter):

    return cv.filter2D(img,-1,filter)

img = np.array(cv.imread('Fig03.tif',0))

horizontal = np.array(((-1,-2,-1),
                       (0, 0, 0),
                       (1, 2, 1)))

vertial = np.array(((-1, 0, 1),
                    (-2, 0, 2),
                    (-1, 0, 1)))

horizontal_img = apply_filter(img, horizontal)
vertial_img = apply_filter(img, vertial)

result = horizontal_img + vertial_img

cv.imshow('Horizontal Sobel',horizontal_img)
cv.imshow('Vertial Sobel', vertial_img)
cv.imshow('Final Image', result)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Horizontal Sobel.png',horizontal_img)
cv.imwrite('Vertial Sobel.png', vertial_img)
cv.imwrite('Final Image.png', result)