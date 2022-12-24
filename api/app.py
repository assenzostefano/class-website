from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from dotenv import load_dotenv
import requests
import os
import urllib
import pymongo

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
    if(request.method == 'GET'):
        collection_find_username = list(collection.find({}, {"School Subject": 1,}))
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
                        "Subject 1": array_username[6],
                        "Subject 2": array_username[7],
                        "Subject 3": array_username[8],
                        "Subject 4": array_username[9],
                        "Subject 5": array_username[10],
                        "Subject 6": array_username[11],
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
                        "Subject 1": array_username[18],
                        "Subject 2": array_username[19],
                        "Subject 3": array_username[20],
                        "Subject 4": array_username[21],
                        "Subject 5": array_username[22],
                        "Subject 6": array_username[23],
                    },
                    "friday": {
                        "Subject 1": array_username[24],
                        "Subject 2": array_username[25],
                        "Subject 3": array_username[26],
                        "Subject 4": array_username[27],
                        "Subject 5": array_username[28],
                        "Subject 6": array_username[29],
                    }
                }
            }

        return jsonify(test)

if __name__ == '__main__':
   app.run()