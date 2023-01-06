# Libraries for open and use Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pymongo
from pymongo import MongoClient
import urllib.parse
import os

USERNAME = ""
PASSWORD = ""
options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')

driver = webdriver.Firefox(options=options)
driver.get("https://nuvola.madisoft.it/login")  # Open Nuvola website

# Click on the username field and insert the username, then click on the password field and insert the password.
username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username")))
password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password")))
# Insert username and password
username.click()
username.clear()
username.send_keys(USERNAME)
password.click()
password.clear()
password.send_keys(PASSWORD)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/button"))).click()  # Click on login button
# Section Vote School
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div[1]/nav/div/div/a[6]"))).click()  # Click on the Compiti button

print(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/p"))).text)