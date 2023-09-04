from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import uuid
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()