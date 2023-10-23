from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from helperfunctions.csvwriter import write_csv_card_links
from tqdm import tqdm
import pandas as pds


def get_elements(link_par):
    try:
        driver.get(link_par)
        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except KeyboardInterrupt:
        image_tags = driver.find_elements()


driver = webdriver.Chrome()
LINK = "https://www.shopltk.com/search?keyword=bedroom&type=post"
elements = get_elements(LINK)