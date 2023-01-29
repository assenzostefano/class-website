from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()
SID = os.getenv('SID')
AUTH_TOKEN = os.getenv('AUTHTOKEN')
PHONE_NUMBER_BOT = os.getenv('PHONE_NUMBER_BOT')
PHONE_NUMBER_PERSONAL = os.getenv('PHONE_NUMBER_PERSONAL')

client = Client(SID, AUTH_TOKEN)

message = client.messages.create(to=PHONE_NUMBER_PERSONAL, 
                                from_=PHONE_NUMBER_BOT, 
                                body="Hello from Python!")