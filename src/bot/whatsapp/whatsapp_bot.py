from selenium.webdriver.firefox.options import Options # Selenium
from selenium import webdriver # Selenium
from dotenv import load_dotenv
from twilio.rest import Client
import time
import subprocess
import os

load_dotenv()
SID = os.getenv('SID')
AUTH_TOKEN = os.getenv('AUTHTOKEN')
PHONE_NUMBER_BOT = os.getenv('PHONE_NUMBER_BOT')
PHONE_NUMBER_PERSONAL = os.getenv('PHONE_NUMBER_PERSONAL')

client = Client(SID, AUTH_TOKEN)

message = client.messages \
                .create(
                     body="Test",
                     media_url=['IMAGE URL'],
                     from_=PHONE_NUMBER_BOT,
                     to=PHONE_NUMBER_PERSONAL
                 )
print(message.sid)