from flask import Flask, render_template, request, session, jsonify, redirect, flash, url_for
from dotenv import load_dotenv
from flask_pymongo import PyMongo
import requests
import urllib
import pymongo
import logging
import bcrypt
import sys
import os

load_dotenv() #Load .env file
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["school-time-table"] #Collection school time table current
collection_archive = database["archive-school-time-table"] #Collection school time table archive

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('PASSWORD_MONGODB')
app.config['MONGO_dbname'] = 'website-class'
app.config['MONGO_URI'] = mongo_url
mongo = PyMongo(app)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        
if __name__ == '__main__':
   app.run()