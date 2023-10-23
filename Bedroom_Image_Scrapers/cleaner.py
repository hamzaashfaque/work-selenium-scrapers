import os
import time
import cv2
import shutil
from tqdm import trange

def display_resized_image(image, height = 720):
    # Display cv2 image after resizing it to fit on screen
    scaling_factor = height/image.shape[0]
    image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)
    cv2.imshow("Image", image)


def image_parser(filedirectory, index=0, end_index = None):
    # Parses through individual images
    ImgList = os.listdir(filedirectory)
    if end_index is None:
        end_index = len(ImgList)

    # Specify the number of classes to move to here
    img_to_move1 = [False] * len(ImgList)
    img_to_move2 = [False] * len(ImgList)
    img_to_move3 = [False] * len(ImgList)

    i=index
    while i < len(ImgList):
        img = cv2.imread(filedirectory + ImgList[i], 1)
        display_resized_image(img, 720)
        print("Image " + str(i+1) + " of " + str(len(ImgList)))
        key = cv2.waitKey(0)

        # Specify here, which key moves to which class
        if key == ord('z'):
            print("To copy to bedroom")
            img_to_move1[i] = True
            i = i+1
        elif key == ord('x'):
            print("To copy to bed")
            img_to_move2[i] = True
            i = i+1
        elif key == ord('c'):
            print("To copy to other")
            img_to_move3[i] = True
            i = i+1
        elif key == 8:
            img_to_move1[i] = False
            img_to_move2[i] = False
            img_to_move3[i] = False
            i = i-1
        elif key == 27:
            print("End program")
            cv2.destroyAllWindows()
            break
        else:
            print("Invalid key")
        cv2.destroyAllWindows()
        time.sleep(0.2)

    # Specify the returned directories
    return img_to_move1, img_to_move2, img_to_move3


def image_copy(input_dir,
               output_list1, output_list2, output_list3,
               output_dir1, output_dir2, output_dir3, index = 0):
    # Copies images to specified directory
    ImgList = os.listdir(input_dir)
    i=index
    for i in trange(len(ImgList)):
        if output_list1[i] is True:
            shutil.copy(src=input_dir + ImgList[i], dst=output_dir1)
        if output_list2[i] is True:
            shutil.copy(src=input_dir + ImgList[i], dst=output_dir2)
        if output_list3[i] is True:
            shutil.copy(src=input_dir + ImgList[i], dst=output_dir3)


# Current project directory
cwd = os.getcwd() + "/"

# Directory from which images are taken
input_file_directory = cwd + "istock_images/"
index = 1706

# Directories to which images are copied
file_directory1 = cwd + "Bedroom/"
file_directory2 = cwd + "Bed/"
file_directory3 = cwd + "Other/"

img1, img2, img3 = image_parser(input_file_directory, index=index)
image_copy(input_file_directory,
           img1, img2, img3,
           file_directory1, file_directory2, file_directory3, index=index)