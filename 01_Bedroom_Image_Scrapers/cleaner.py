import os
import time
import cv2
import shutil

def image_parser(filedirectory1, filedirectory2, index=0):
    #parses through individual images
    ImgList = os.listdir(filedirectory1)
    ImgToMove = [None] * len(ImgList)
    i=index
    while i < len(ImgList):
        print(filedirectory1 + ImgList[i])
        img = cv2.imread(filedirectory1 + ImgList[i], 1)
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Image", img)
        print("Image " + str(i+1) + " of " + str(len(ImgList)))
        key = cv2.waitKey(0)
        if key == 13:
            print("To Copy")
            ImgToMove[i] = True
            shutil.copy2(filedirectory1 + ImgList[i], filedirectory2 + ImgList[i])
            i = i+1
        elif key == 32:
            print("To Keep")
            ImgToMove[i] = False
            i = i+1
        else:
            print("Invalid key")
        cv2.destroyAllWindows()
        time.sleep(1)

#current project directory
cwd = os.getcwd() + "/"
#The directory from which files are to be moved
filedirectory1 = cwd + "images_bedroom/"
#The directory to which files are to be moved
filedirectory2 = cwd + "images_other/"

image_parser(filedirectory1, filedirectory2)