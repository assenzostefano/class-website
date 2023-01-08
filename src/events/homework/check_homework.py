# Libraries for open and use Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

# Libraries for MongoDB and .env file
from pymongo import MongoClient
from dotenv import load_dotenv
import urllib.parse
import pymongo
import time
import os

#Load .env file
load_dotenv()
USERNAME = os.getenv('USERNAME_NUVOLA') #Username for Nuvola
PASSWORD = os.getenv('PASSWORD_NUVOLA') #Password for Nuvola
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["homework"] #Collection school time table current

options = Options()
options.add_argument("--headless") # Headless mode (so you don't see the browser)
options.add_argument('--disable-gpu') # Disable GPU
driver = webdriver.Firefox(options=options) # Open Firefox and set options

def giorno_cinque():
    #Giorno cinque
    try:
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]"))).text) # Date
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/p"))).text) # Homework 1 or no homework
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li/h2"))).text) # School subject 1
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            driver.close()
    except TimeoutException:
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/h2"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            driver.close()

def giorno_quattro():
    #Giorno quattro
    try:
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]"))).text) # Date
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/p"))).text) # Homework 1 or no homework
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li/h2"))).text) # School subject 1
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            giorno_cinque()
    except TimeoutException:
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/h2"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            giorno_cinque()

def giorno_tre():
    #Giorno tre
    try:
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]"))).text) # Date
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/p"))).text) # Homework 1 or no homework
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li/h2"))).text) # School subject 1
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            giorno_quattro()
    except TimeoutException:
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/h2"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            giorno_quattro()

def giorno_due():
    #Giorno due
    try:
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]"))).text) # Date
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/p"))).text) # Homework 1 or no homework
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li/h2"))).text) # School subject 1
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            giorno_tre()
    except TimeoutException:
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/h2"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            giorno_tre()

def giorno_uno():
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

    #Giorno uno
    try:
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]"))).text) # Date
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/p"))).text) # Homework 1 or no homework
        print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li/h2"))).text) # School subject 1
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            giorno_due()
    except TimeoutException:
        try:
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/h2"))).text) # School subject 1
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4

            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            print(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            giorno_due()

giorno_uno()

#Compiti solo uno
# /html/body/div/div/main/div/p

# Compiti più di uno
# /html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p
# /html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p

# Giorno dopo
# /html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]


# Nome Materia solo una
# /html/body/div/div/main/div/div[2]/div/ul/li/h2

# Nome Materia più di una
# /html/body/div/div/main/div/div[2]/div/ul/li[1]/h2
# /html/body/div/div/main/div/div[2]/div/ul/li[2]/h2