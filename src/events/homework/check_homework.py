import pymongo
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from dotenv import load_dotenv
import os
import urllib.parse
import time

# Disable GPU for Firefox
options = Options()
options.add_argument('--disable-gpu')

# Disable showing Firefox window
options.headless = True

load_dotenv() #Load .env file
USERNAME = os.getenv('USERNAME_NUVOLA') #Username for Nuvola
PASSWORD = os.getenv('PASSWORD_NUVOLA') #Password for Nuvola
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
# Initialize the browser with the given options
browser = webdriver.Firefox(options=options)

# Wait for up to 10 seconds for elements to appear
wait = WebDriverWait(browser, 10)

# Connect to the MongoDB database
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
db = client["website-class"]

# Get today's date as a string in the format "YYYY-MM-DD"
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Get the collection for today's data
collection = db["homework"]

# Initialize the URL for Cloud
url = 'https://nuvola.madisoft.it/login'

browser.get(url)
username = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, "username")))  # Wait for the username input
password = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, "password")))  # Wait for the password input
username.click()
username.clear()
username.send_keys(USERNAME)  # Insert username
password.click()
password.clear()
password.send_keys(PASSWORD)  # Insert password
WebDriverWait(browser, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/button"))).click() # Click on login button
# Section Homework
WebDriverWait(browser, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/nav/div/div/a[6]"))).click() # Click on homework button

# Click on the "Next Day" button to go to the next day's tasks
next_day_button = WebDriverWait(browser, 250).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]')))

def wait_recheck():
    time.sleep(10800)

def check_homework():
    for i in range(1, 10):
        try:
            text1 = str(WebDriverWait(browser, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text)
            print(text1)
            text1 = str(WebDriverWait(browser, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text)
            print(text1)
            text1 = str(WebDriverWait(browser, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text)
            print(text1)
            text1 = str(WebDriverWait(browser, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text)
            print(text1)
            text1 = str(WebDriverWait(browser, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text)
            print(text1)
            WebDriverWait(browser, 250).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]'))).click() # Click on next day button
        except:
            try:
                text = str(WebDriverWait(browser, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/p"))).text)
                print(text)
                WebDriverWait(browser, 250).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]'))).click() # Click on next day button
            except:
                WebDriverWait(browser, 250).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]'))).click() # Click on next day button

    browser.quit()
    wait_recheck()

check_homework()