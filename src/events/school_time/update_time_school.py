from bson.objectid import ObjectId
from dotenv import load_dotenv
import openpyxl as xl
import datetime
import pymongo
import urllib
import os

load_dotenv() #Load .env file
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["school-time-table"] #Collection school time table current
collection_archive = database["archive-school-time-table"] #Collection school time table archive

x = collection.delete_many({}) #Delete all documents in collection (school-time-table)

# Load excel file
namefile_xlsx = "attachments/school_time.xlsx"
workbook = xl.load_workbook(filename=namefile_xlsx)
ws = workbook.active

#Date
current_time = datetime.datetime.now()
day = str(current_time.day)
month = str(current_time.month)
year = str(current_time.year)
hour = str(current_time.hour)
minute = str(current_time.minute)
long_date = day + "-" + month + "-" + year + " " + hour + ":" + minute

#Create collection
mydict = { 
    "Date": long_date,
    "School Subject": [],
    "Teacher": [],
}
x = collection.insert_one(mydict) # Add collection on collection (school-time-table)
x = collection_archive.insert_one(mydict) # Add collection on collection (archive-school-time-table)

#Search my class in excel file and add in MongoDB
for row in range (1, 100):
    # column B ~ column F
    for column in range (1, 100):
        cell = ws.cell(row, column)
        if cell.value == "2elci":
            ws.cell(row=cell.row, column=column).value
            #Search school time table
            for i in range(4,80):
                school_subject = ws.cell(row=i, column=column).value # Get school subject from excel file
                if school_subject == 0: #If school subject is 0, add "null" in MongoDB
                    find_document_username = list(collection.find({}, {"Date": long_date})) #Find document in MongoDB
                    array_username = find_document_username[0]["_id"]
                    collection.update_one( # Add "null" in MongoDB beacause school subject is 0
                        { "_id": ObjectId(array_username)},
                            {
                                "$push": { "School Subject": "null" }
                            }
                        )
                    collection_archive.update_one( # Add "null" in MongoDB beacause school subject is 0
                        { "_id": ObjectId(array_username)},
                            {
                                "$push": { "School Subject": "null" }
                            }
                        )
                else: #If school subject is not 0, add school subject in MongoDB
                    #remove_things_in_front = school_subject.split(' ', 1)[1]
                    find_document_username = list(collection.find({}, {"Date": long_date})) #Find document in MongoDB
                    array_username = find_document_username[0]["_id"]
                    collection.update_one( # Add school subject in MongoDB beacause school subject is not 0
                        { "_id": ObjectId(array_username)},
                            {
                                "$push": { "School Subject": school_subject }
                            }
                        )
                    collection_archive.update_one( # Add school subject in MongoDB beacause school subject is not 0
                        { "_id": ObjectId(array_username)},
                            {
                                "$push": { "School Subject": school_subject }
                            }
                        )
                        
            #Search teacher
            for i in range(4, 80):
                teacher = ws.cell(row=i, column=column+1).value
                column = column
                if teacher == 0: #If teacher is 0, add "null" in MongoDB
                    find_document_username = list(collection.find({}, {"Date": long_date})) #Find document in MongoDB
                    array_username = find_document_username[0]["_id"]
                    collection.update_one( # Add "null" in MongoDB beacause teacher is 0
                        { "_id": ObjectId(array_username)},
                            {
                                "$push": { "Teacher": "null" }
                            }
                        )
                    collection_archive.update_one( # Add "null" in MongoDB beacause teacher is 0
                        { "_id": ObjectId(array_username)},
                            {
                                "$push": { "Teacher": teacher }
                            }
                        )
                else: #If teacher is not 0, add teacher in MongoDB
                    find_document_username = list(collection.find({}, {"Date": long_date}))
                    array_username = find_document_username[0]["_id"]
                    collection.update_one( # Add teacher in MongoDB beacause teacher is not 0
                        { "_id": ObjectId(array_username)},
                            {
                                "$push": { "Teacher": teacher }
                            }
                        )
                    collection_archive.update_one( # Add teacher in MongoDB beacause teacher is not 0
                        { "_id": ObjectId(array_username)},
                            {
                                "$push": { "Teacher": teacher }
                            }
                        )

os.remove(namefile_xlsx) #Delete excel file