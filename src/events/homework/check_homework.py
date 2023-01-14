# Import file for check homework
from day_one import day_one

# Libraries for open and use Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

# Libraries for MongoDB and .env file
from dotenv import load_dotenv
import urllib.parse
import pymongo
import os

#Load .env file
load_dotenv() #Load .env file
USERNAME = os.getenv('USERNAME_NUVOLA') #Username for Nuvola
PASSWORD = os.getenv('PASSWORD_NUVOLA') #Password for Nuvola
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["homework"] #Collection school time table current

# Options for Firefox
options = Options() # Set options
options.add_argument("--headless") # Headless mode (so you don't see the browser)
options.add_argument('--disable-gpu') # Disable GPU

def start_search():
    global driver
    driver = webdriver.Firefox(options=options) # Open Firefox and set options
    driver.get("https://nuvola.madisoft.it/login")  # Open Nuvola website
    username = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "username")))  # Wait for the username input
    password = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "password")))  # Wait for the password input

    username.click()
    username.clear()
    username.send_keys(USERNAME)  # Insert username
    password.click()
    password.clear()
    password.send_keys(PASSWORD)  # Insert password
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/button"))).click() # Click on login button

    # Section Homework
    WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/nav/div/div/a[6]"))).click() # Click on homework button
    homework_check()

def homework_check():
    #Giorno uno
    day_five.giorno_cinque(driver, collection)
    driver.close()
    start_search()

start_search()