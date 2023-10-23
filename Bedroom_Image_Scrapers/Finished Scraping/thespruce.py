from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from helperfunctions.csvwriter import write_csv_card_links, write_csv
from tqdm import tqdm
import time


def get_card_links(link_par):
    card_links = []
    driver.get(link_par)
    driver.implicitly_wait(5)
    a_tags = driver.find_elements(By.CLASS_NAME, "mntl-card-list-items")
    for tag in a_tags:
        link_string = tag.get_attribute("href")
        if link_string not in card_links:
            card_links.append(link_string)
    return card_links


def get_image_links(card_links):
    img_url = []
    img_titles = []
    for card in tqdm(card_links):
        driver.get(card)
        time.sleep(2)
        driver.implicitly_wait(5)
        tags = driver.find_elements(By.CSS_SELECTOR, ".figure-media > div > img")
        for tag in tqdm(tags):
            driver.execute_script("arguments[0].scrollIntoView();", tag)
            time.sleep(1)
        title = driver.find_element(By.CLASS_NAME, "heading__title").get_attribute("innerHTML").replace("\n", " ").strip()
        tags = driver.find_elements(By.CSS_SELECTOR, ".figure-media > div > img")
        try:
            url_string = driver.find_element(By.CSS_SELECTOR, ".primary-image__media > div > img").get_attribute("src")
        except:
            url_string = ""
        for tag in tags:
            tag_string = tag.get_attribute("src")
            try:
                url_string = url_string + " | " + tag_string
            except:
                continue
        img_titles.append(title)
        img_url.append(url_string)
    return img_url, img_titles


driver = webdriver.Chrome()
#LINK = "https://www.thespruce.com/bedroom-design-4127963"
#card_links = get_card_links(link_par=LINK)
#write_csv_card_links(card_links=card_links, filename="thespruce_links.csv")

df1 = pd.read_csv("thespruce_links.csv", encoding="ISO-8859-1")
card_links = df1["card_link"].to_list()
img_url, img_titles = get_image_links(card_links)
write_csv(card_links, img_url, img_titles, "thespruce.csv")