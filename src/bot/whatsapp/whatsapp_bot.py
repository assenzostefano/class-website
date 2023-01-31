from selenium.webdriver.firefox.options import Options # Selenium
from selenium import webdriver # Selenium
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()
SID = os.getenv('SID')
AUTH_TOKEN = os.getenv('AUTHTOKEN')
PHONE_NUMBER_BOT = os.getenv('PHONE_NUMBER_BOT')
PHONE_NUMBER_PERSONAL = os.getenv('PHONE_NUMBER_PERSONAL')

client = Client(SID, AUTH_TOKEN)

options = Options() # Set options
options.add_argument("--headless") # Headless mode (so you don't see the browser)
options.add_argument('--disable-gpu') # Disable GPU
options.add_argument('window-size=1024x768')
driver = webdriver.Firefox(options=options)
driver.get('http://127.0.0.1:4999/orario')
driver.get_screenshot_as_file("screenshot.png")
driver.quit()
message = client.messages \
                .create(
                     body="Test",
                     media_url=['IMAGE URL'],
                     from_=PHONE_NUMBER_BOT,
                     to=PHONE_NUMBER_PERSONAL
                 )
print(message.sid)