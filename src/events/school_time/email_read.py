from update_time_school import update_time_school

from dotenv import load_dotenv
from imbox import Imbox
import urllib.parse
import traceback
import pathlib
import pymongo
import time
import os

# Load .env file
load_dotenv()

HOST = os.getenv('IMAP_SERVER') #IMAP server
USERNAME = os.getenv('EMAIL') #Username (ex . test@example.com)
PASSWORD = os.getenv('PWD_EMAIL') #IMAP Password
DOWNLOAD_FOLDER = os.getenv('DOWNLOAD_FOLDER') #Download folder for xlsx file
EMAIL_SCHOOL = os.getenv('EMAIL_SCHOOL') #Email school
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["email"] #Collection school time table current

def recheck_email(): # Every 10 seconds check if there is a new email
    time.sleep(600)
    check_email()

def check_email():
    try:
        if not os.path.isdir(DOWNLOAD_FOLDER):
            os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

        mail = Imbox(HOST, username=USERNAME, password=PASSWORD, ssl=True, ssl_context=None, starttls=False) # Connect to IMAP Server
        messages = mail.messages(sent_from=EMAIL_SCHOOL, unread=True) # Get unread emails from school

        for (uid, message) in messages:
            mail.mark_seen(uid)

            # Download attachments
            for idx, attachment in enumerate(message.attachments):
                try:
                    att_fn = attachment.get('filename') # Get attachment filename
                    download_path = f"{DOWNLOAD_FOLDER}/{att_fn}"
                    extension_file = pathlib.Path(att_fn).suffix # Get extension file
                    print(extension_file)
                    if extension_file != ".xlsx": # Check if file is xlsx
                        print("Check file")
                    else:
                        if collection.find_one({"filename": att_fn}):
                            print("File already exists")
                        else:
                            with open(download_path, "wb") as fp:
                                fp.write(attachment.get('content').read())
                                os.rename(download_path, f"{DOWNLOAD_FOLDER}/school_time.xlsx") # Rename file
                                collection.delete_many({}) # Delete old file
                                collection.insert_one({"filename": att_fn}) # Insert filename to MongoDB
                                update_time_school() # Update school time table
                except:
                    print(traceback.print_exc())

        mail.logout() # Logout from email
        recheck_email() 
    except:
        print(traceback.print_exc())
        recheck_email()