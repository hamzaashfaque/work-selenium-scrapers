"""
Outlined here are the instructions for how to use this script

The .csv file specified as the input must have the following columns
img_url

If a single entry has multiple image links, the links must be written in a
single string seperated by a "|" character.

Use the script from cmd terminal as follows:
python urldownloader.py "(input file here)" "(output directory here)" --start (starting index) --end (ending index)

The output directory must be present in order for code to work
"""


import pandas as pd
import argparse
import requests
import io
import os
import shutil
from tqdm import tqdm, trange


def get_input(input_filepath, start_idx = None, end_idx = None):
    # Gets the dataframe from .csv file, along with start and end idx
    df = pd.read_csv(input_filepath, encoding="ISO-8859-1",
                     index_col=None, skipinitialspace=True)
    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(df)-1
    start_idx = int(start_idx)
    end_idx = int(end_idx)
    if start_idx > len(df)-1 or start_idx < 0:
        raise Exception("Start Index out of bounds")
    if end_idx > len(df)-1 or end_idx < 0:
        raise Exception("End Index out of bounds")
    return df, start_idx, end_idx


def download_img(dataframe, start_idx, end_idx, output_dir):
    # Downloads images from csv file and save them in output_dir directory
    url_strings = []
    url_list = dataframe["img_url"].to_list()
    pbar = trange(0, len(url_list))
    pbar.update(start_idx)
    i = start_idx
    while i<= end_idx:
        url_strings = url_list[i].replace(" ", "").split('|')
        for url in tqdm(url_strings):
            if len(url) == 0:
                continue
            save_url_image(url, output_dir,
                            index1=i, index2=url_strings.index(url))
        pbar.update(1)
        i += 1
    print("Downloading Complete!")


def save_url_image(url, output_dir, index1, index2):
    # Saves the image given in the url
    filename = str(index1).zfill(6) + "_" + str(index2).zfill(4)
    try:
        image_content = requests.get(url, timeout=20)
    except (requests.exceptions.ConnectionError,
            requests.exceptions.InvalidSchema,
            requests.exceptions.Timeout,
            requests.exceptions.ChunkedEncodingError) as error:
        print(f"\nError at index [{str(index1)}][{str(index2)}]: {error}")
        return
    output_dir.replace("\\", "")
    output_dir.replace("/", "")
    dir_path = os.getcwd() + "\\" + output_dir
    filepath = dir_path + "\\" + filename + ".png"
    with open(filepath, "wb") as f:
        f.write(image_content.content)
    


parser = argparse.ArgumentParser()
parser.add_argument("input_file",
                    help="Specify .csv file from which to download images")
parser.add_argument("output_directory",
                    help="Specify output directory to save downloaded images")
parser.add_argument("--start",
                    help="Specify the starting index of the pandas dataframe")
parser.add_argument("--end",
                    help="Specify the ending index of the pandas dataframe")
args = parser.parse_args()


df, str_idx, end_idx = get_input(args.input_file, args.start, args.end)
download_img(df, str_idx, end_idx, args.output_directory)