import os
import shutil
import pandas as pd
from tqdm import tqdm


def get_data(input_dir):
    data = os.listdir(input_dir)
    text_data = []
    for value in tqdm(data):
        if ".txt" in value:
            text_data.append(value)
    return text_data


def separate_data(text_data, input_dir):
    separated_txt = []
    separated_img = []
    for file in tqdm(text_data):
        df = pd.read_csv(input_dir + file, index_col=None, sep=" ")
        if 6 in df.iloc[:, 0].tolist():
            separated_txt.append(file)
            separated_img.append(file.replace(".txt", ".jpg"))
    return separated_txt, separated_img


def copy_data(separated_data, input_dir, output_dir_txt, output_dir_img):
    for file in tqdm(separated_data):
        if ".txt" in file:
            shutil.copy(src=input_dir+file, dst=output_dir_txt)
        elif ".jpg" in file:
            shutil.copy(src=input_dir+file, dst=output_dir_img)


# Current project directory
cwd = os.getcwd() + "/"

# Directory from which images are taken
input_directory = cwd + "input/"

# Directories to which images are copied
output_dir_txt = cwd + "output/"
output_dir_img = cwd + "output2/"

text_data = get_data(input_directory)
text_data, img_data = separate_data(text_data, input_directory)
separated_data = text_data + img_data
copy_data(separated_data, input_directory, output_dir_txt, output_dir_img)