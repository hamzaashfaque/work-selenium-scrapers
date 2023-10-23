#https://www.get.furniture/bedroom/bedroom-sets.html?product_list_limit=75
#https://www.get.furniture/bedroom/bedroom-sets.html?p=2&product_list_limit=75


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from helperfunctions.csvwriter import write_csv
import time
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def get_page_links(link):
    card_links = []
    for i in range(1, 5):
        driver.get(link + str(i) + "&product_list_limit=75")
        driver.implicitly_wait(5)
        anchor_tags = driver.find_elements(By.CSS_SELECTOR, ".filterproducts > li > div > div > a")
        for tag in anchor_tags:
            card_links.append(tag.get_attribute("href"))
    return card_links

def get_image_urls(card_links):
    url_list = []
    for card in card_links:
        url = ""
        driver.get(card)
        driver.implicitly_wait(10)
        img_buttons = driver.find_elements(By.CLASS_NAME, "fotorama__nav__frame--thumb")
        for button in img_buttons:
            time.sleep(2)
            url = url + driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]").get_attribute("href") + " | "
        url_list.append(url)
    return(url_list)
            

link = "https://www.get.furniture/bedroom/bedroom-sets.html?p="

#card_links = get_page_links(link=link)

print(get_image_urls(["https://www.get.furniture/mirror-bed-group-bedroom-set-in-chocolate.html"]))