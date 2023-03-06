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
    time.sleep(60)
    send_notification()

def send_notification():
    today = datetime.datetime.today().strftime('%A')
    tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%A')
    now = datetime.datetime.now()
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
                    bot.send_message(b, str(i['School Subject'][today][0]['Room']) + ", " + i['School Subject'][today][0]['Teacher'] + ", " + i['School Subject'][today][0]['Subject'] + "\n" + "Successiva: " + str(i['School Subject'][today][1]['Room']) + ", " + i['School Subject'][today][1]['Teacher'] + ", " + i['School Subject'][today][1]['Subject'])
            recheck()
        elif now.strftime("%H:%M") == "08:50":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, str(i['School Subject'][today][1]['Room']) + ", " + i['School Subject'][today][1]['Teacher'] + ", " + str(i['School Subject'][today][1]['Subject']) + "\n" + "Successiva: " + str(i['School Subject'][today][2]['Room']) + ", " + i['School Subject'][today][2]['Teacher'] + ", " + i['School Subject'][today][2]['Subject'])
            recheck()
        elif now.strftime("%H:%M") == "09:50":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, str(i['School Subject'][today][2]['Room']) + ", " + i['School Subject'][today][2]['Teacher'] + ", " + str(i['School Subject'][today][2]['Subject']) + "\n" + "Successiva: " + str(i['School Subject'][today][3]['Room']) + ", " + i['School Subject'][today][3]['Teacher'] + ", " + i['School Subject'][today][3]['Subject'])
            recheck()
        elif now.strftime("%H:%M") == "11:05":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, str(i['School Subject'][today][3]['Room']) + ", " + i['School Subject'][today][3]['Teacher'] + ", " + str(i['School Subject'][today][3]['Subject']) + "\n" + "Successiva: " + str(i['School Subject'][today][4]['Room']) + ", " + i['School Subject'][today][4]['Teacher'] + ", " + i['School Subject'][today][4]['Subject'])
            recheck()
        elif now.strftime("%H:%M") == "12:05":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, str(i['School Subject'][today][4]['Room']) + ", " + i['School Subject'][today][4]['Teacher'] + ", " + str(i['School Subject'][today][4]['Subject']) + "\n" + "Successiva: " + str(i['School Subject'][today][5]['Room']) + ", " + i['School Subject'][today][5]['Teacher'] + ", " + i['School Subject'][today][5]['Subject'])
            recheck()
        elif now.strftime("%H:%M") == "13:05":
            for i in find_document:
                for b in array_username:
                    bot.send_message(b, str(i['School Subject'][today][5]['Room']) + ", " + i['School Subject'][today][5]['Teacher'] + ", " + str(i['School Subject'][today][5]['Subject']))
            recheck()
        elif now.strftime("%H:%M") == "21:00":
            if tomorrow == "Sunday" or tomorrow == "Saturday":
                print("Nope")
            else:
                for i in find_document:
                    for b in array_username:
                        bot.send_message(b, i['School Subject'][tomorrow][0]['Subject'] + ", " + i['School Subject'][tomorrow][0]['Teacher'] + "\n" + i['School Subject'][tomorrow][1]['Subject'] + ", " + i['School Subject'][tomorrow][1]['Teacher'] + "\n" + i['School Subject'][tomorrow][2]['Subject'] + ", " + i['School Subject'][tomorrow][2]['Teacher'] + "\n" + i['School Subject'][tomorrow][3]['Subject'] + ", " + i['School Subject'][tomorrow][3]['Teacher'] + "\n" + i['School Subject'][tomorrow][4]['Subject'] + ", " + i['School Subject'][tomorrow][4]['Teacher'] + "\n" + i['School Subject'][tomorrow][5]['Subject'] + ", " + i['School Subject'][tomorrow][5]['Teacher'])
        else:
            recheck()

schedule.every().day.at("16:25").do(send_notification)
now = datetime.datetime.now()
t1 = threading.Thread(target=bot.polling).start()

while True:
    schedule.run_pending()
