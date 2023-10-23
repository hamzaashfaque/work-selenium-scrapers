from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from helperfunctions.csvwriter import write_csv
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
import time

#https://www.ashleyfurniture.com/c/furniture/sets/bedroom-sets/?start=0&sz=48
#0-48-96......288-336
#0-1-2.....6

#img link + $AFHS-PDP-Main$

def get_card_links():
    #for getting card links
    card_links = []
    link = "https://www.ashleyfurniture.com/c/furniture/sets/bedroom-sets/?start="
    for i in range(0, 7):
        driver.get(link + str(i*48) + "&sz=48")
        time.sleep(3)
        driver.implicitly_wait(5)
        anchor_tags = driver.find_elements(By.CLASS_NAME, "thumb-link")
        for tag in anchor_tags:
            card_links.append(tag.get_attribute("href"))
        print(card_links)

#def get_image_url():
    #for getting image urls and titles

card_links = get_card_links()