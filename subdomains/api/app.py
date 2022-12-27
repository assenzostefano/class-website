from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from dotenv import load_dotenv
import requests
import os
import urllib
import pymongo
import datetime
import requests
import time

app = Flask(__name__)

load_dotenv() #Load .env file
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["school-time-table"]

@app.route('/', methods = ['GET', 'POST'])
def api():
    current_time = datetime.datetime.now()
    day = str(current_time.day)
    month = str(current_time.month)
    year = str(current_time.year)
    hour = str(current_time.hour)
    minute = str(current_time.minute)
    long_date = day + "-" + month + "-" + year + hour + ":" + minute
    collection_find_username = list(collection.find({}, {"Date": long_date ,"School Subject": 1,}))
    array_username = collection_find_username[0]['School Subject']

    test = {
            "subject" : {
                "monday": {
                    "Subject 1": array_username[0],
                    "Subject 2": array_username[1],
                    "Subject 3": array_username[2],
                    "Subject 4": array_username[3],
                    "Subject 5": array_username[4],
                    "Subject 6": array_username[5],
                },
                "tuesday": {
                    "Subject 1": array_username[14],
                    "Subject 2": array_username[15],
                    "Subject 3": array_username[16],
                    "Subject 4": array_username[17],
                    "Subject 5": array_username[18],
                    "Subject 6": array_username[19],
                },
                "wednesday": {
                    "Subject 1": array_username[12],
                    "Subject 2": array_username[13],
                    "Subject 3": array_username[14],
                    "Subject 4": array_username[15],
                    "Subject 5": array_username[16],
                    "Subject 6": array_username[17],
                },
                "thursday": {
                    "Subject 1": array_username[28],
                    "Subject 2": array_username[29],
                    "Subject 3": array_username[30],
                    "Subject 4": array_username[31],
                    "Subject 5": array_username[32],
                    "Subject 6": array_username[33],
                },
                "friday": {
                    "Subject 1": array_username[42],
                    "Subject 2": array_username[43],
                    "Subject 3": array_username[44],
                    "Subject 4": array_username[45],
                    "Subject 5": array_username[46],
                    "Subject 6": array_username[47],
                }
            }
        }

    return jsonify(test)

if __name__ == '__main__':
   app.run()