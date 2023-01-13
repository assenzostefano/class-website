# Libraries for MongoDB and .env file
from dotenv import load_dotenv
import urllib.parse
import pymongo
import os
import datetime

#Load .env file
load_dotenv()
USERNAME = os.getenv('USERNAME_NUVOLA') #Username for Nuvola
PASSWORD = os.getenv('PASSWORD_NUVOLA') #Password for Nuvola
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["homework"] #Collection school time table current

mydict = {
  "subjects": [
    {
      "name": "Stefanologia",
      "homework": [
        {
          "date": {
            "day": str(12),
            "month": str(1),
            "year": str(2023),
          },
          "description": "Niente compiti yeeee",
        }
      ]
    }
  ]
},
string = "11 january 2023"
a = string.split()
b = a[0]
print(b)
#x = collection.insert_many(mydict) # Insert data in MongoDB

# {
#  "subjects": [
#    {
#      "name": "Disegno",
#      "homework": [
#        {
#          "date": {
#            "day": 12,
#            "month": 1,
#            "year": 2023
#          },
#          "description": "Per le vacanze di natale..."
#        }
#      ]
#    }
#  ]
#}