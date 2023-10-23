from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
from helperfunctions.csvwriter import write_csv_card_links, write_csv
from tqdm import tqdm
import pandas as pd
import time


def get_card_links(link_par):
    number_of_links = 0
    card_links = []
    driver.get(link_par)
    actions = ActionChains(driver)
    try:
        while(True):
            driver.implicitly_wait(4)
            time.sleep(2)
            tags = driver.find_elements(By.XPATH, "//*[@class='masonry__item']/div[1]/div[2]/div[1]/a")
            for tag in tags:
                link_text = tag.get_attribute("href")
                if link_text not in card_links:
                    card_links.append(link_text)
                    number_of_links += 1
                    print(number_of_links)
                if tag == tags[-1]:
                    actions.move_to_element(tag).perform()
    except KeyboardInterrupt:
        return card_links


def get_image_links(card_links):
    image_links = []
    titles = []
    for link in tqdm(card_links):
        driver.get(link)
        driver.implicitly_wait(5)
        tags = driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/main/div/div[2]/div/div[1]/div/div[2]/div[2]/div//img")
        title = driver.find_element(By.CLASS_NAME, "ltk-caption").get_attribute("innerHTML").replace('\n', ' ').strip()
        titles.append(title)
        try:
            img_string = driver.find_element(By.XPATH, "//*[@data-test-id = 'ltk-item/image']//img").get_attribute("src")
        except exceptions.NoSuchElementException:
            print("tag not found")
            img_string = ""
        for tag in tags:
            img_string += " | " + tag.get_attribute("src")
        image_links.append(img_string)
    return image_links, titles


driver = webdriver.Chrome()
#LINK = "https://www.shopltk.com/search?keyword=bedroom&type=post"
#card_links = get_card_links(link_par=LINK)
# write_csv_card_links(card_links=card_links,
#                      filename="shopltk_card_links1.csv")

card_links = pd.read_csv("shopltk_card_links1.csv",
                         encoding="ISO-8859-1",
                         index_col=None).iloc[:, 0].to_list()
image_links, titles = get_image_links(card_links)
write_csv(card_links, image_links, titles, filename="shopltk.csv")