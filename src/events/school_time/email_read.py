import os
from imbox import Imbox
import traceback


host = os.getenv('SMTP_SERVER')
username = os.getenv('EMAIL')
password = os.getenv('PWD_EMAIL')
download_folder = os.getenv('DOWNLOAD_FOLDER')
EMAIL_SCHOOL = os.getenv('EMAIL_SCHOOL')

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
    
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(sent_from=EMAIL_SCHOOL)

for (uid, message) in messages:
    mail.mark_seen(uid) # optional, mark message as read

    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')
            download_path = f"{download_folder}/{att_fn}"
            print(download_path)
            with open(download_path, "wb") as fp:
                fp.write(attachment.get('content').read())
        except:
            print(traceback.print_exc())

mail.logout()