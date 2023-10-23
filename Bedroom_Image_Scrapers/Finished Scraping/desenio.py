from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
from helperfunctions.csvwriter import write_csv
from tqdm import tqdm, trange
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def get_card_links(link_par):
    card_links = []
    driver.get(link_par)
    driver.implicitly_wait(4)
    a_tags = driver.find_elements(By.CLASS_NAME, "pinterest-enabled")
    for tag in a_tags:
        try:
            link_string = tag.get_attribute("href")
            if link_string not in card_links:
                card_links.append(link_string)
        except:
            continue
    return card_links


def get_image_links(card_links):
    images = []
    titles = []
    for link in tqdm(card_links):
        driver.get(link)
        images.append(driver.find_element(By.CSS_SELECTOR, "#synapse-photoswipe-14 > a").get_attribute("href"))
        titles.append(link.split("/")[6])
    return images, titles


LINK = "https://desenio.co.uk/g/gallery-walls/bedroom/?page=3"
card_links = get_card_links(link_par=LINK)
img_links, img_titles = get_image_links(card_links=card_links)
write_csv(card_links, img_links, img_titles, "desenio.csv")
driver.close()
print("Scraping Completed!")