from bson.objectid import ObjectId
from dotenv import load_dotenv
from telebot import telebot
import threading
import datetime
import schedule
import pymongo
import urllib
import time
import os

load_dotenv()
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["subscribe"] #Collection school time table current
collection_schooltime = database["school-time-table"] #Collection school time table current
API_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, I'm a bot")

@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    take_id = message.from_user.id #Get user id
    #Insert the id of the user who writes /subscribe in the database
    find_document_username = list(collection.find({}, {"_id": 1}))
    array_username = find_document_username[0]["_id"]
    collection.update_one(
        { "_id": ObjectId(array_username)},
            {
                "$push": { "username": take_id }
            }
    )
    bot.send_message(message.chat.id, "You are subscribed")

def recheck():
    time.sleep(1)
    send_notification()

def send_notification():
    # Inserisci il giorno di oggi
    today = datetime.datetime.today().strftime('%A')
    # Print hours
    now = datetime.datetime.now()
    print(now.strftime("%H:%M"))
    finish = False
    if today == "Saturday" or today == "Sunday":
        print("Today is weekend")
    else:
        # Alla prima ora (7.50) manda una notifica a tutti gli utenti che hanno scritto /subscribe della materia della prima ora e così via
        find_document = list(collection_schooltime.find({}, {"_id": 0, "School Subject": 1}))
        collection_find_username = list(collection.find({}, {"username": 1,})) #Find all username in collection
        array_username = collection_find_username[0]["username"] #Array with all username
        #gaga = find_document['School Subject'][today][0]['Subject']
        print(now.strftime("%H:%M"))
        if now.strftime("%H:%M") == "07:50":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, i['School Subject'][today][0]['Subject'])
        elif now.strftime("%H:%M") == "08:53":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, i['School Subject'][today][1]['Subject'])
        elif now.strftime("%H:%M") == "09:53":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, i['School Subject'][today][2]['Subject'])
        elif now.strftime("%H:%M") == "10:53":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, i['School Subject'][today][3]['Subject'])
        elif now.strftime("%H:%M") == "12:08":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, i['School Subject'][today][4]['Subject'])
        elif now.strftime("%H:%M") == "13:08":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, i['School Subject'][today][5]['Subject'])
        else:
            recheck()

schedule.every().day.at("07:50").do(send_notification)
now = datetime.datetime.now()
t1 = threading.Thread(target=bot.polling).start()

while True:
    print(now.strftime("%H:%M"))
    schedule.run_pending()
