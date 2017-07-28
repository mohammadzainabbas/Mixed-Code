import numpy as np
import cv2
from skimage import feature
from sklearn import neighbors
from sklearn.svm import SVC
import imutils
import glob
import matplotlib.pyplot as plt
import csv
import random

Data = []
print('Processing:')
##with open('Features.csv', 'w') as csvfile:
i = 0
for img in glob.glob("D:/Fahad/NOTES/DIP Lec/Assignment3/texture1/*.tiff"):
    image = cv2.imread(img,0)
    s = '\n\tTex1 Image: '+str(i+1)
    print(s)
    i = i+1
    image = cv2.resize(image,(512,512))
    rows,c = np.shape(image)

    Features = []

    GLCM = feature.greycomatrix(image, [1], [0])

    contrast = feature.greycoprops(GLCM, prop='contrast')
    homogeneity = feature.greycoprops(GLCM, prop='homogeneity')


    FT = np.fft.fft2(image)

    shifted = np.fft.fftshift(FT)

    norm = np.zeros((rows,c),dtype = np.double)
    R,C = np.shape(norm)

    cv2.normalize(np.abs(shifted), norm, 0, 255, cv2.NORM_MINMAX, -1)

    th_hist = np.zeros(4);

    angles = [0, 45, 90, 135];

    for nmbr in range(0,len(angles)):
        rotated = imutils.rotate_bound(norm, angles[nmbr])
        
        R2,C2 = np.shape(rotated)
        temp = 0
        for j in range(int(C2/2), C2):
            temp = temp +rotated[int(R2/2), j]
            
        th_hist[nmbr] = temp
            
    r_hist = np.zeros(256)

    for k in range(1,256):
        chunk = norm[int(rows/2)-k:int(rows/2)+k+1 , int(c/2)-k:int(c/2)+k+1]
        dimR , dimC = np.shape(chunk)
        r_hist[k-1] =  np.sum(chunk[0,:]) + np.sum(chunk[dimR-1,:]) + np.sum(chunk[1:dimR-1,0]) + np.sum(chunk[1:dimR-1,dimC-1])

    r_hist = np.around(r_hist, decimals=2);
    th_hist = np.around(th_hist, decimals=2);
    temp = []
    temp.append(contrast[0][0])
    temp.append(homogeneity[0][0])
    temp.extend(r_hist)
    temp.extend(th_hist)
    temp.append(0)
    
    Data.append(temp);
##        writer = csv.writer(csvfile, delimiter=',')
##        writer.writerow([str(contrast[0][0]),str(homogeneity[0][0]),str(th_hist),str(r_hist),str(0)])

i = 0
for img in glob.glob("D:/Fahad/NOTES/DIP Lec/Assignment3/texture2/*.tiff"):
    image = cv2.imread(img,0)
    s = '\n\tTex2 Image: '+str(i+1)
    print(s)
    i = i+1
    image = cv2.resize(image,(512,512))
    rows,c = np.shape(image)

    GLCM = feature.greycomatrix(image, [1], [0])

    contrast = feature.greycoprops(GLCM, prop='contrast')
    homogeneity = feature.greycoprops(GLCM, prop='homogeneity')


    FT = np.fft.fft2(image)

    shifted = np.fft.fftshift(FT)

    norm = np.zeros((rows,c),dtype = np.double)
    R,C = np.shape(norm)

    cv2.normalize(np.abs(shifted), norm, 0, 255, cv2.NORM_MINMAX, -1)

    th_hist = np.zeros(4);

    angles = [0, 45, 90, 135];

    for nmbr in range(0,len(angles)):
        rotated = imutils.rotate_bound(norm, angles[nmbr])
        
        R2,C2 = np.shape(rotated)
        temp = 0
        for j in range(int(C2/2), C2):
            temp = temp +rotated[int(R2/2), j]
            
        th_hist[nmbr] = temp
            
    r_hist = np.zeros(256)

    for k in range(1,256):
        chunk = norm[int(rows/2)-k:int(rows/2)+k+1 , int(c/2)-k:int(c/2)+k+1]
        dimR , dimC = np.shape(chunk)
        r_hist[k-1] =  np.sum(chunk[0,:]) + np.sum(chunk[dimR-1,:]) + np.sum(chunk[1:dimR-1,0]) + np.sum(chunk[1:dimR-1,dimC-1])

    r_hist = np.around(r_hist, decimals=2);
    th_hist = np.around(th_hist, decimals=2);

    
    temp = []
    temp.append(contrast[0][0])
    temp.append(homogeneity[0][0])
    temp.extend(r_hist)
    temp.extend(th_hist)
    temp.append(1)
    
    Data.append(temp);
##        writer = csv.writer(csvfile, delimiter=',')
##        writer.writerow([str(contrast[0][0]),str(homogeneity[0][0]),str(th_hist),str(r_hist),str(1)])

print('Trained')


def KNN():
    random.shuffle(Data)

    features = []
    classes = []
    for subset in Data:
        
        features.append(subset[0: len(subset)-2]);
        classes.append(float(subset[len(subset)-1]))        
    
    half = int(len(Data)/2)

    Train_features = features[0:half]
    Train_classes = classes[0:half]

    Test_features = features[half:len(Data)]
    Test_classes = classes[half:len(Data)]

    classifier = neighbors.KNeighborsClassifier(n_neighbors=5)
    classifier.fit(Train_features, Train_classes)
    result = classifier.predict(Test_features)
    print('Classes of Test samples:\n',Test_classes)
    print('\nPredicted Classes of Test samples:\n',result)
   
    C_M(Test_classes,result)

Subset_length = 0
def MD():

    data_test = []
    
    half = int(len(Data)/2)
    for subset in Data:
        Subset_length = len(subset)
        break;

    M0 = np.zeros((Subset_length))
    M1 = np.zeros((Subset_length))

    
    for k in range(0,12):
        if k <6:
            for j in range(0,Subset_length-1):
                M0[j] = M0[j]+(Data[k][j])
                
                M1[j] = M1[j]+(Data[k+6][j])
                
        else:
            data_test.append(Data[k])
            data_test.append(Data[k+6])


    M0 = M0/6
    M1 = M1/6

    random.shuffle(data_test)

    rand = random.sample(range(0, 6), 3)

    test_classes = []
    predicted_classes = []
    for value in range(0,len(data_test)):
        test_sampl = data_test[value]

        test_classes.append(data_test[value][Subset_length-1])
        temp1 = 0
        temp2 = 0
        
        for j in range(0,Subset_length):
            temp1 = temp1 + np.square((test_sampl[j]) - (M0[j]))
            temp2 = temp2 + np.square((test_sampl[j]) - (M1[j]))

        E_distance = []
        E_distance.append(np.sqrt(temp1))
        E_distance.append(np.sqrt(temp2))
        
        Class = np.argmin(E_distance)
        predicted_classes.append(Class)

    print('Test Classes:\n',test_classes)
    print('Predicted Classes:\n',predicted_classes)
    C_M(test_classes,predicted_classes)

def SVM():
    random.shuffle(Data)

    features = []
    classes = []
    for subset in Data:
        
        features.append(subset[0: len(subset)-2]);
        classes.append(float(subset[len(subset)-1]))        
    
    half = int(len(Data)/2)

    Train_features = features[0:half]
    Train_classes = classes[0:half]

    Test_features = features[half:len(Data)]
    Test_classes = classes[half:len(Data)]

    classifier = SVC()
    classifier.fit(Train_features, Train_classes)
    result = classifier.predict(Test_features)
    print('Classes of Test samples:\n',Test_classes)
    print('\nPredicted Classes of Test samples:\n',result,'\n')
   
    C_M(Test_classes,result)


def C_M(Actual, Predicted):
    c_m = np.zeros((2,2))
    for i in range(len(Predicted)):
        c_m[int(Actual[i]),int(Predicted[i])] = c_m[int(Actual[i]),int(Predicted[i])] + 1

    print('Confusion Mtrix:\n', c_m)
    print('\nAccuracy: ',(c_m[0,0]+c_m[1,1]*100)/np.sum(c_m),'%\n')
