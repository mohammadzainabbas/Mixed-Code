import matplotlib.pyplot as mtp
import numpy as np
import cv2 as cv
x= np.array
x= cv.imread("testImg.jpg",0)
y= np.array
y= cv.imread("testImg.jpg",0)


cv.imshow("Task1", x)

a=np.shape(x)
row= int(a[0])
col=int( a[1])

z = np.zeros((row,col),dtype=np.uint8)
w = np.zeros((row,col),dtype=np.uint8)

b=np.mean (x)
print(b)

for i in range(0, (row-1)):
    for j in range(0, (col-1)):
        if((x[i,j]) > b):  #compare current pixel with mean value
            y[i,j]=255   #white
        else:
            y[i,j]= 0  #black

for i in range(0, (row-1)):
    for j in range(0, (col-1)):
        r= int(x[i,j])
        s= int((256-1)-r)  #formula given #256==L
        z[i,j]= s   #assign s value in z array

#negative ka black and white
for i in range(0, (row-1)):
    for j in range(0, (col-1)):
        if((z[i,j]) > b):  #compare current pixel with mean value
            w[i,j]=255   #white
        else:
            w[i,j]= 0  #black




cv.imshow("black and white" , y)
cv.imshow("negative" , z)
cv.imshow("negative ka BW" , w)

            
        
        


