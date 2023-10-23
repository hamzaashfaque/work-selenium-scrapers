from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from helperfunctions.csvwriter import write_csv, write_csv_card_links, write_number_of_items_done
from tqdm import trange
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


def get_card_links(link_par):
    card_links = []
    for i in trange(1, 251):
        link = link_par + str(i)
        driver.get(link)
        driver.implicitly_wait(4)
        a_tags = driver.find_elements(By.CLASS_NAME, "listing-link")
        for tag in a_tags:
            try:
                link_string = tag.get_attribute("href")
                if link_string not in card_links:
                    card_links.append(link_string)
            except:
                continue
    return card_links


def get_image_links(card_links):
    img_links = []
    img_titles = []
    for link in card_links:
        driver.get(link)
        driver.implicitly_wait(4)
        img_tags = driver.find_elements(By.CSS_SELECTOR, ".scroll-container-no-scrollbar > ul > li > img")
        try:
            title = driver.find_element(By.XPATH, "//*[@id='listing-page-cart']/div/h1").get_attribute("innerHTML")
        except:
            title = link.split("/")[5]
        img_links_string = ""
        for tag in img_tags:
            link_string = tag.get_attribute("src")
            link_string = link_string.replace("il_75x75", "il_NxN")
            img_links_string = img_links_string + " | " + link_string
        img_links.append(img_links_string)
        img_titles.append(title)
    return img_links, img_titles


LINK = "https://www.etsy.com/c/home-and-living/bedding?ref=pagination&page="
#card_links = get_card_links(link_par=LINK)
#write_csv_card_links(card_links=card_links, filename="etsy_cards.csv")


START_IDX = 7010
str_idx = START_IDX
increment = 10
end_idx = str_idx + increment

df1 = pd.read_csv("etsy_cards.csv", encoding="ISO-8859-1")
card_links = df1["card_link"].to_list()
try:
    df2 = pd.read_csv("etsy.csv", encoding="ISO-8859-1")
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
    write_csv(card_links[0:end_idx], img_links, img_titles, "etsy.csv")
    str_idx = end_idx
    if end_idx + increment > final_entry:
        increment = 1
        end_idx += increment
    else:
        end_idx += increment
    pbar.update(increment)
    write_number_of_items_done(str_idx, "etsy_num.txt")
driver.close()
pbar.close()
print("Scraping Completed!")