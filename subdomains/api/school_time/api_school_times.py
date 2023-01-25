from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient
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
mongo_url = "mongodb+srv://elci:gWB3EL%25W%405%5EA%40PGvvYRt@stefano-cluster.iphin.mongodb.net/website-class"
print(mongo_url) #URL for MongoDB (with password)
client = MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["school-time-table"]
db = client.get_database()

@app.route("/", methods=["GET"])
def get_subjects():
    schedule_collection = db.schedule

    # Utilizza il metodo find() per recuperare tutti i documenti della collezione
    # e li converte in una lista
    schedule = list(schedule_collection.find())

    # Restituisce la risposta come una stringa JSON
    return jsonify(schedule)


if __name__ == '__main__':
   app.run()