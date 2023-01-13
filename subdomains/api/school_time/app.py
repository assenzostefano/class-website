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
    long_date = day + "-" + month + "-" + year + " " + hour + ":" + minute
    #Search school subject
    collection_find_schoolsubject = list(collection.find({}, {"Date": long_date ,"School Subject": 1,}))
    array_schoolsubject = collection_find_schoolsubject[0]['School Subject']
    #Search teacher
    collection_find_teacher = list(collection.find({}, {"Date": long_date ,"Teacher": 1,}))
    array_teacher = collection_find_teacher[0]['Teacher']

    test = {
            "subject" : {
                "monday": {
                    "Subject 1": array_schoolsubject[0],
                    "Subject 2": array_schoolsubject[1],
                    "Subject 3": array_schoolsubject[2],
                    "Subject 4": array_schoolsubject[3],
                    "Subject 5": array_schoolsubject[4],
                    "Subject 6": array_schoolsubject[5],
                },
                "tuesday": {
                    "Subject 1": array_schoolsubject[14],
                    "Subject 2": array_schoolsubject[15],
                    "Subject 3": array_schoolsubject[16],
                    "Subject 4": array_schoolsubject[17],
                    "Subject 5": array_schoolsubject[18],
                    "Subject 6": array_schoolsubject[19],
                },
                "wednesday": {
                    "Subject 1": array_schoolsubject[12],
                    "Subject 2": array_schoolsubject[13],
                    "Subject 3": array_schoolsubject[14],
                    "Subject 4": array_schoolsubject[15],
                    "Subject 5": array_schoolsubject[16],
                    "Subject 6": array_schoolsubject[17],
                },
                "thursday": {
                    "Subject 1": array_schoolsubject[28],
                    "Subject 2": array_schoolsubject[29],
                    "Subject 3": array_schoolsubject[30],
                    "Subject 4": array_schoolsubject[31],
                    "Subject 5": array_schoolsubject[32],
                    "Subject 6": array_schoolsubject[33],
                },
                "friday": {
                    "Subject 1": array_schoolsubject[42],
                    "Subject 2": array_schoolsubject[43],
                    "Subject 3": array_schoolsubject[44],
                    "Subject 4": array_schoolsubject[45],
                    "Subject 5": array_schoolsubject[46],
                    "Subject 6": array_schoolsubject[47],
                },
            },
            "teacher": {
                "monday": {
                    "Teacher 1": array_teacher[0],
                    "Teacher 2": array_teacher[1],
                    "Teacher 3": array_teacher[2],
                    "Teacher 4": array_teacher[3],
                    "Teacher 5": array_teacher[4],
                    "Teacher 6": array_teacher[5],
                },
                "tuesday": {
                    "Teacher 1": array_teacher[14],
                    "Teacher 2": array_teacher[15],
                    "Teacher 3": array_teacher[16],
                    "Teacher 4": array_teacher[17],
                    "Teacher 5": array_teacher[18],
                    "Teacher 6": array_teacher[19],
                },
                "wednesday": {
                    "Teacher 1": array_teacher[28],
                    "Teacher 2": array_teacher[29],
                    "Teacher 3": array_teacher[30],
                    "Teacher 4": array_teacher[31],
                    "Teacher 5": array_teacher[32],
                    "Teacher 6": array_teacher[33],
                },
                "thursday": {
                    "Teacher 1": array_teacher[42],
                    "Teacher 2": array_teacher[43],
                    "Teacher 3": array_teacher[44],
                    "Teacher 4": array_teacher[45],
                    "Teacher 5": array_teacher[46],
                    "Teacher 6": array_teacher[47],
                },
                "friday": {
                    "Teacher 1": array_teacher[56],
                    "Teacher 2": array_teacher[57],
                    "Teacher 3": array_teacher[58],
                    "Teacher 4": array_teacher[59],
                    "Teacher 5": array_teacher[60],
                    "Teacher 6": array_teacher[61],
                },
            },
        }

    return jsonify(test)

if __name__ == '__main__':
   app.run()