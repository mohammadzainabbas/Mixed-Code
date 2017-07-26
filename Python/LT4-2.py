import matplotlib.pyplot as mtp
import numpy as np
import cv2 as cv

x= np.array
x= cv.imread("fig01.tif",0)
#cv.imshow("original", x)

#cv.imshow("Task1", x)

b=np.power(x, 0.9)

a=np.shape(x)
row= int(a[0])
col=int( a[1])

#xmin= np.min(x)
#xmax= np.max(x)

s= np.zeros((row,col),dtype=np.uint8)
#t= np.zeros((row,col),dtype=np.uint8)
#u= np.zeros((row,col),dtype=np.uint8)
v= np.zeros((row,col),dtype=np.float)   #powwr and log ki values are in float
#so un kay lye float data type
vv= np.zeros((row,col),dtype=np.uint8)

def power():  #gamma ki val increase means darker image
    for i in range(0, row):
        for j in range(0,col):
        #    s[i,j]=np.power(x[i,j], 0.9)
         #   s[i,j] = (((s[i,j] - xmin )*255) / (xmax-xmin));
       #     t[i,j]=np.power(x[i,j], 0.6)
       #     u[i,j]=np.power(x[i,j], 1.3)

            v[i,j]=np.power(x[i,j], 1.8)

    xmin= np.min(v)   #jo image bani hy power formuala say us ki max aur min val nikalni h
    xmax= np.max(v)
    for i in range(0, row):
        for j in range(0,col):
            vv[i,j] = ((float(v[i,j] - xmin )) / (xmax-xmin))*255;  #normalization formual
        

   # cv.imshow("Power", s)
  #  cv.imshow("Power1", t)
  #  cv.imshow("Power2", u)
    cv.imshow("Power3", vv)

def log():
    for i in range(0, row):
        for j in range(0,col):
            s[i,j]=100*np.log10 (1+x[i,j])

    xmin= np.min(s)    #min max for s wali image which was log wala formula use kr k 
    xmax= np.max(s)
    for i in range(0, row):
        for j in range(0,col):
            s[i,j] = (((s[i,j] - xmin )*255) / (xmax-xmin));
            
    
    cv.imshow("original", x)
    cv.waitKey()
    cv.imshow("LOg", s)
   




#normalization = x-xmin / xmax- xmin



