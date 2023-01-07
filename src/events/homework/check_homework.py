# Libraries for open and use Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
collection = database["school-time-table"] #Collection school time table current

# Settings for Firefox
options = Options()
options.add_argument("--headless") # Headless mode (so you don't see the browser)
options.add_argument('--disable-gpu') # Disable GPU

driver = webdriver.Firefox(options=options) # Open Firefox and set options
driver.get("https://nuvola.madisoft.it/login") # Open Nuvola website

def recheck():
    time.sleep(10)
    check_homework()

def connect_to_nuvola():
    try:
        username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username"))) # Wait for the username input
        password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))) # Wait for the password input

        username.click()
        username.clear()
        username.send_keys(USERNAME) # Insert username
        password.click()
        password.clear()
        password.send_keys(PASSWORD) # Insert password
        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/button"))).click() # Click on login button

        # Section Homework
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/nav/div/div/a[6]"))).click() # Click on homework button
    except:
        print("Error in login")

def check_homework():
    next_homework = 0
    if next_homework == 10:
        print("ao basta")
    else:
        date = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]"))) # Print the date
        print(date.text())
        try:
            homework_1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p")))
            print(homework_1.text())
            try:
                homework_2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p")))
                print(homework_2.text())
                try:
                    homework_3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p")))
                    print(homework_3.text())
                    try:
                        homework_4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p")))
                        print(homework_4.text())
                        try:
                            homework_5 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p")))
                            print(homework_5.text())
                        except:
                            print("Homework 5 not found")
                            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]/svg"))).click() # Click on next day button
                            next_homework += 1
                            check_homework()
                    except:
                        print("Homework 4 not found")
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]/svg"))).click() # Click on next day button
                        next_homework += 1
                        check_homework()
                except:
                    print("Homework 3 not found")
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]/svg"))).click() # Click on next day button
                    next_homework += 1
                    check_homework()
            except:
                print("Homework 2 not found")
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]/svg"))).click() # Click on next day button
                next_homework += 1
                check_homework()
        except:
            print("No homework")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]/svg"))).click() # Click on next day button
            next_homework += 1
            check_homework()

#Date
# /html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]
# /html/body/div/div/main/div/div[1]/div[1]/div[1]/div[1]/button[1]

#Button for next day
# /html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]/svg
# /html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]/svg

#Compiti
# /html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p
# /html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p
# /html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p

#Se non ci sono compiti
# /html/body/div/div/main/div/p