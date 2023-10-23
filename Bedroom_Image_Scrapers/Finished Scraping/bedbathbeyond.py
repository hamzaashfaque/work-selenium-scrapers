from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import uuid
import csv
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

def page_links_grabber():
    #grabs all links from all pages
    card_links = []
    link = "https://www.bedbathandbeyond.com/c/bedding/bedding-sets?t=276&page="
    for i in range(1, 85):
        try:
            driver.get(link + str(i))
            driver.implicitly_wait(5)
            anchor_tags = driver.find_elements(By.CLASS_NAME, "productTile_link__zHGHe")
            for tag in anchor_tags:
                card_links.append(tag.get_attribute("href"))
            print("page "+ str(i) +" success!")
        except:
            print("fail at: "+ link + str(i))
    return card_links

def card_scrapper(card_link):
    #scraps individual links
    driver.get(card_link)
    driver.implicitly_wait(3)
    url_string = ""
    title = ""
    # buttons = driver.find_elements(By.CLASS_NAME, "css-k5nm06")
    # for button in buttons:
    #     driver.execute_script("arguments[0].click();", button)
    #     driver.implicitly_wait(1)
    #     url_string = url_string +" | "+ driver.find_element(By.CSS_SELECTOR, "#page-wrap > main > div > div > div.center-gutter-left.css-10sjjsc > div > div.css-1fq7d03.e16sgn6119 > div.css-15x5cbk.e16sgn6117 > div > div.css-6n1ert.e1ao6o5k0 > div > img").get_attribute("src")
    title = driver.find_element(By.TAG_NAME, "title").get_attribute("innerHTML").replace(',', ' ')
    url_string = driver.find_element(By.CSS_SELECTOR, "#page-wrap > main > div > div > div.center-gutter-left.css-10sjjsc > div > div.css-1fq7d03.e16sgn6119 > div.css-15x5cbk.e16sgn6117 > div > div.css-6n1ert.e1ao6o5k0 > div > img").get_attribute("src")
    return url_string, title

def write_csv(card_links, img_links, img_titles, filename):
    #Writes links into csv file
    with open(filename, mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "card_link", "title", "img_url"])
        writer.writeheader()
        for i in range(len(card_links)):
            writer.writerow({"card_link":card_links[i], "img_url":img_links[i], "id":uuid.uuid1(), "title":img_titles[i]})

card_links = page_links_grabber()
print("links = "+str(len(card_links)))
img_urls = []
img_titles = []

for link in card_links:
    try:
        url, title = card_scrapper(link)
        img_urls.append(url)
        img_titles.append(title)
        print("success for: " + title)
    except:
        img_urls.append("")
        img_titles.append("")
        print("fail at: "+link)

write_csv(card_links, img_urls, img_titles, "bedbathbeyond.csv")