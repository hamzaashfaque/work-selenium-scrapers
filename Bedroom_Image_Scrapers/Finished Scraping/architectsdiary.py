from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from helperfunctions.csvwriter import write_csv, write_csv_card_links, write_number_of_items_done
from tqdm import trange, tqdm
from selenium.common import exceptions
import time
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def get_card_links(link_par):
    card_links = []
    driver.get(link_par)
    driver.implicitly_wait(4)
    a_tags = driver.find_elements(By.CSS_SELECTOR, ".pd-blog-details > figure > a")
    for tag in a_tags:
        link_string = tag.get_attribute("href")
        card_links.append(link_string)
    return card_links

def get_image_links(card_links):
    img_links = []
    img_titles = []
    for link in card_links:
        driver.get(link)
        driver.implicitly_wait(4)
        img_tags = driver.find_elements(By.XPATH, "//div[@class='pd-left-bg']//img")
        for tag in tqdm(img_tags):
            driver.execute_script("arguments[0].scrollIntoView();", tag)
            time.sleep(0.1)
        img_tags = driver.find_elements(By.XPATH, "//div[@class='pd-left-bg']//img")
        try:
            title = driver.find_element(By.CLASS_NAME, "atc-details-main--title").get_attribute("innerHTML")
        except:
            title = link.split("/")[3]
        img_links_string = ""
        for tag in img_tags:
            link_string = tag.get_attribute("src")
            img_links_string = img_links_string + " | " + link_string
        img_links.append(img_links_string)
        img_titles.append(title)
    return img_links, img_titles


# LINK = "https://thearchitectsdiary.com/modern-bedroom-design-inspiration/"
# card_links = get_card_links(link_par=LINK)
# write_csv_card_links(card_links=card_links, filename="archidiary_cards.csv")

START_IDX = 92
str_idx = START_IDX
increment = 1
end_idx = str_idx + increment

df1 = pd.read_csv("archidiary_cards.csv", encoding='ISO-8859-1')
card_links = df1["card_link"].to_list()
try:
    df2 = pd.read_csv("archidiary.csv", encoding='ISO-8859-1')
    img_links = df2["img_url"].to_list()
    img_titles = df2["title"].to_list()
except FileNotFoundError:
    img_links = []
    img_titles = []
final_entry = len(card_links)

pbar = trange(0, len(card_links))
pbar.update(str_idx)
while(end_idx < final_entry):
    links, titles = get_image_links(card_links=card_links[str_idx:end_idx])
    img_links = img_links + links.copy()
    img_titles = img_titles + titles.copy()
    write_csv(card_links[0:end_idx], img_links, img_titles, "archidiary.csv")
    str_idx = end_idx
    if end_idx + increment > final_entry:
        increment = 1
        end_idx += increment
    else:
        end_idx += increment
    pbar.update(increment)
    write_number_of_items_done(str_idx, "archidiary_num.txt")
driver.close()
pbar.close()
print("Scraping Completed!")