import subprocess
import os
import tabula
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
LINK_SCHOOL_TIME = os.getenv('LINK_SCHOOL_TIME')
FILE_DIRECTORY_SCHOOL = os.getenv('FILE_DIRECTORY_SCHOOL')
options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')

driver = webdriver.Firefox(options=options)
#url launch
driver.get(LINK_SCHOOL_TIME)
#identify link with partial link text

elems = driver.find_elements(By.XPATH, "/html/body/section[2]/div/div/main/div/div/div/div/div[2]/p[2]/a")

for elem in elems:
    link = elem.get_attribute("href")

remove_things_in_front = link.split(FILE_DIRECTORY_SCHOOL, 1)[1]
print(remove_things_in_front)
subprocess.run(["wget", link])

driver.close()

namefile = remove_things_in_front
df = tabula.read_pdf(namefile, pages = 'all')[0]
tabula.convert_into(namefile, "test.csv", output_format="csv", pages='all')
print(df)

from pyexcel.cookbook import merge_all_to_a_book
# import pyexcel.ext.xlsx # no longer required if you use pyexcel >= 0.2.2 
import glob


merge_all_to_a_book(glob.glob("*.csv"), "school_time.xlsx")