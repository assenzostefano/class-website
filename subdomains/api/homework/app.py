from flask import Flask, jsonify
from dotenv import load_dotenv
import urllib.parse
import pymongo
import os

load_dotenv() #Load .env file
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["homework"] #Collection school time table current

app = Flask(__name__)

@app.route('/homework')
def get_homework():
    homework = collection.find({}, {"_id": 0})
    return jsonify(list(homework))
if __name__ == '__main__': 
   app.run()