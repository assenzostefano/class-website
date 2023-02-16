from urllib.request import Request, urlopen
from flask import Flask, render_template, url_for, request, redirect, session, flash, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import bcrypt
import urllib
from pymongo import MongoClient
import logging
import json
import sys
import os

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("src/log/all.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

app = Flask(__name__)
app.secret_key = "testing"
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
client = MongoClient("mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["school-time-table"] #Collection school time table current

@app.route('/')
def homepage():
    logging.info("A user went up: Homepage")
    dict = list(collection.find({}, {"_id": 0, "School Subject": 1}))
    return render_template('homepage.html', data=dict)
    #imageList = os.listdir('static/images')
    #imageList = ['images/' + image for image in imageList]
    #return render_template('go.html', imageList=imageList)

@app.route('/orario')
def orario():
    logging.info("A user went up: Orario")
    #url = "http://127.0.0.1:5000"
    #response = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    #webpage = urlopen(response).read()
    # Take all data from mongodb
    dict = list(collection.find({}, {"_id": 0, "School Subject": 1}))
    number = str(range(0,7))
    day = str(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    return render_template('orario/orario.html', data=dict, number=number, day=day)
        
# #connect to your Mongo DB database
def MongoDB():
    client = MongoClient("mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB)
    db = client.get_database('website-class')
    records = db.users
    return records

records = MongoDB()


#assign URLs to have a particular route 
@app.route("/register", methods=['post', 'get'])
def register():
    message = ''
    #if method post in index
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        #if found in database showcase that it's found 
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('index.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('index.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('index.html', message=message)
        else:
            #hash the password and encode it
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            #assing them in a dictionary in key value pairs
            user_input = {'name': user, 'email': email, 'password': hashed}
            #insert it in the record collection
            records.insert_one(user_input)
            
            #find the new created account and its email
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            #if registered redirect to logged in as the registered user
            return render_template('logged_in/logged_in.html', email=new_email)
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #check if email exists in database
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            #encode the password and check if it matches
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Wrong password'
                return render_template('login/login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login/login.html', message=message)
    return render_template('login/login.html', message=message)

@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('logged_in/logged_in.html', email=email)
    else:
        return redirect(url_for("login"))

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("signout/signout.html")
    else:
        return render_template('index.html')

if __name__ == '__main__':
   logging.info("Web server started!") 
   app.run(port=4999, debug=True)