import os
from imbox import Imbox
from dotenv import load_dotenv
import traceback
import time

# Load .env file
load_dotenv()

HOST = os.getenv('IMAP_SERVER') #IMAP server
USERNAME = os.getenv('EMAIL') #Username (ex . test@example.com)
PASSWORD = os.getenv('PWD_EMAIL') #IMAP Password
DOWNLOAD_FOLDER = os.getenv('DOWNLOAD_FOLDER') #Download folder for xlsx file
EMAIL_SCHOOL = os.getenv('EMAIL_SCHOOL') #Email school

def recheck_email(): # Every 10 seconds check if there is a new email
    time.sleep(10)
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
                    with open(download_path, "wb") as fp:
                        fp.write(attachment.get('content').read())
                        os.rename(download_path, f"{DOWNLOAD_FOLDER}/school_time.xlsx") # Rename file
                except:
                    print(traceback.print_exc())

        mail.logout() # Logout from email
        recheck_email() 
    except:
        print(traceback.print_exc())
        recheck_email()