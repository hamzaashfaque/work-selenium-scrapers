from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from helperfunctions.csvwriter import write_csv
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def page_links_grabber():
    #grabs all links from all pages
    url_links = []
    titles = []
    link = "https://www.marlofurniture.com/collections/bedroom-sets?page="
    for i in range(1, 22):
        try:
            driver.get(link + str(i))
            driver.implicitly_wait(5)
            image_tags = driver.find_elements(By.CSS_SELECTOR, ".product-grid-image > img")
            titles_tags = driver.find_elements(By.CLASS_NAME, "product_title")
            for j in range(len(image_tags)):
                url_links.append(image_tags[j].get_attribute("src"))
                titles.append(titles_tags[j].get_attribute("innerHTML").replace(',', ' '))
            print("Page " + str(i))
        except:
            print("fail at: "+ link + str(i))
    return url_links, titles

links, titles = page_links_grabber()
write_csv(links, links, titles, "marlofurniture.csv")