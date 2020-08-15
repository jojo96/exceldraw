import cv2
import pandas as pd
import easygui
import unicodedata
import numpy as np
    
def excelDraw():
    
    #Only one argument image path
    #For example: if path = 'C:\Users\admin\Downloads\rf.jpg'
    #You can call exceldraw(path)
    #Returns: 2 dataframes
    #It works like this:
    #do, dd =  exceldraw(path)
    #do.to_csv('C:\Users\admin\Downloads\file12.csv'), can change download path
    #dd.to_csv('C:\Users\admin\Downloads\file22.csv')
    
    uni_img = easygui.fileopenbox()
    img_path = unicodedata.normalize('NFKD', uni_img)
    img = cv2.imread(img_path)
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, bw) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    bwo = cv2.resize(bw,(128,512))
    do = pd.DataFrame(np.zeros((bwo.shape[0], bwo.shape[1])))
    dd = pd.DataFrame(np.ones((bwo.shape[0], bwo.shape[1])))
    for i in range(bwo.shape[0]):
        for j in range(bwo.shape[1]):
            if bwo[i][j]==255:
                do.at[i,j] = 1
                dd.at[i,j] = 0
    return do,dd