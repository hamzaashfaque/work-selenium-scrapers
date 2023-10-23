from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from helperfunctions.csvwriter import write_csv_card_links, write_csv
from tqdm import trange, tqdm


def get_card_links(link_par):
    card_links = []
    for i in trange(1, 5):
        link = link_par + str(i)
        driver.get(link)
        driver.implicitly_wait(4)
        a_tags = driver.find_elements(By.XPATH, "//div[@class='box product']//a[@class='product_card']")
        for tag in a_tags:
            try:
                link_string = tag.get_attribute("href")
                if link_string not in card_links:
                    card_links.append(link_string)
            except:
                continue
    return card_links


def get_image_links(card_links):
    img_url = []
    img_titles = []
    for card in tqdm(card_links):
        driver.get(card)
        driver.implicitly_wait(5)
        title = driver.find_element(By.XPATH, "//h1[@itemprop='name']").get_attribute("innerHTML").replace("\n", " ").strip()
        tags = driver.find_elements(By.CSS_SELECTOR, ".flickity-slider>.product-image--cell>div>a")
        url_string = ""
        for tag in tags:
            url_string = url_string + " | " + tag.get_attribute("href")
        img_titles.append(title)
        img_url.append(url_string)
    return img_url, img_titles


driver = webdriver.Chrome()
#LINK = "https://megafurnitureusa.com/collections/bedroom-bedroom-sets?page="
#card_links = get_card_links(link_par=LINK)
#write_csv_card_links(card_links=card_links, filename="megafurniture_card_links.csv")

df1 = pd.read_csv("megafurniture_card_links.csv", encoding="ISO-8859-1")
card_links = df1["card_link"].to_list()
img_url, img_titles = get_image_links(card_links)
write_csv(card_links, img_url, img_titles, "megafurniture.csv")