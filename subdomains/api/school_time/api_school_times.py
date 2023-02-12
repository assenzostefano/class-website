from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import urllib
import os

app = Flask(__name__)
load_dotenv() #Load .env file
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["school-time-table"]

@app.route("/", methods=["GET"])
def get_subjects():
    subjects = collection.find({}, {"_id": 0})

    #Return all subjects
    return jsonify(list(subjects))

if __name__ == '__main__':
   app.run(debug=True)