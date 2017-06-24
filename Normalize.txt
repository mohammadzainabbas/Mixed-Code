def Normalize(img):
    r,c = np.shape(img)

    img_min = np.min(img)

    #To normalize image
    for i in range(r):
        for j in range(c):
            img[i,j] = img[i,j] - img_min
            
    img_max = np.max(img)
    for i in range(r):
        for j in range(c):
            img[i,j] = 255*(img[i,j]/img_max)
    return img