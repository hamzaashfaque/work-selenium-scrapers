from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from helperfunctions.csvwriter import write_csv
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

def img_scrapper():
    #scraps image urls
    links = []
    images = driver.find_elements(By.CLASS_NAME, "smalllinkimage1")
    for image in images:
        links.append(image.get_attribute("src"))
    return links

def title_scrapper():
    #scraps image titles
    titles = []
    titlestags = driver.find_elements(By.CLASS_NAME, "itemcolor")
    for tag in titlestags:
        titles.append(tag.get_attribute("innerHTML").replace(',', ' '))
    return titles

driver.get("https://www.dallasdesignerfurniture.com/category_1/all/Bedroom.htm")
driver.implicitly_wait(20)
images = img_scrapper()
titles = title_scrapper()
print(len(images))
print(len(titles))
write_csv(images, images, titles, "dallasdesignerfurniture.csv")
