from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import uuid
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get("https://www.potterybarn.com/shop/shop-by-room/bedrooms/")
driver.implicitly_wait(5)

def get_card_links():
    #Gets card links from the bedroom page
    card_links = []
    card_tags = driver.find_elements(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/ul//a")
    for tag in card_tags:
        card_links.append(tag.get_attribute("href")[0:-2])
    return card_links

def browse_card_links(card_links):
    #Browses individual card link and opens it to copy the image url along with their title
    img_links = []
    for link in card_links:
        driver.get(link)
        driver.implicitly_wait(3)
        try:
            img_links.append(driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[2]/div/img").get_attribute("src"))
        except:
            print("xpath error at: " + link)
            img_links.append("")
            continue
    return img_links

def write_csv(card_links, img_links):
    #Writes links into csv file
    with open('potterybarn.csv', mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "card_link", "title", "img_url"])
        writer.writeheader()
        for i in range(len(card_links)):
            writer.writerow({"card_link":card_links[i], "img_url":img_links[i], "id":uuid.uuid1()})

def get_titles_from_url(card_links):
    #uses urls to get titles
    titles = []
    for link in card_links:
        j = link.split("/")
        titles.append(j[-1])
    return titles

def write_titles(img_titles):
    #Writes titles into csv file
    with open('potterybarn_titles.csv', mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["title"])
        writer.writeheader()
        for i in range(len(card_links)):
            writer.writerow({"title":img_titles[i]})

card_links = get_card_links()
img_links = browse_card_links(card_links)
write_csv(card_links, img_links)
img_titles = get_titles_from_url(card_links)
write_titles(img_titles)
print(img_titles)