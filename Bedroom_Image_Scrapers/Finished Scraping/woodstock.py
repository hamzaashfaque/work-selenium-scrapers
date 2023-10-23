from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from helperfunctions.csvwriter import write_csv
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def web_clicker():
    driver.find_element(By.ID, "h374").click()
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[3]/div[1]/div[1]/section/form/fieldset/ul/li[3]/div[2]/table/tbody/tr[2]/td[1]/input").click()
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[3]/div[1]/div[1]/section/form/fieldset/ul/li[3]/div[2]/table/tbody/tr[3]/td[1]/input").click()
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[3]/div[1]/div[1]/section/form/fieldset/ul/li[3]/div[2]/table/tbody/tr[4]/td[1]/input").click()
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[3]/div[1]/div[1]/section/form/fieldset/ul/li[3]/div[2]/table/tbody/tr[5]/td[1]/input").click()
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[3]/div[1]/div[1]/section/form/fieldset/ul/li[3]/div[2]/table/tbody/tr[6]/td[1]/input").click()
    driver.find_element(By.ID, "bottompagesele").click()
    driver.find_element(By.XPATH, "//*[@id='bottompagesele']/option[4]").click()

def get_image_links():
    cards = []
    urls = []
    titles = []
    images = driver.find_elements(By.CSS_SELECTOR, ".ProImgHref > img")
    title_tags = driver.find_elements(By.CSS_SELECTOR, ".ProImgHref > span")
    for i in range(len(images)):
        urls.append(images[i].get_attribute('src').replace('thumbnails', 'images'))
        titles.append(title_tags[i].get_attribute('innerHTML').replace(',', ' '))
    return urls, titles


driver.get("https://www.woodstockvaluecenter.com/category/bedrooms")
driver.implicitly_wait(5)
web_clicker()
urls, titles = get_image_links()
write_csv(urls, urls, titles, "woodstock.csv")