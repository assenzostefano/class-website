from bson.objectid import ObjectId
from openpyxl.styles import NamedStyle
from dotenv import load_dotenv
import openpyxl as xl
import datetime
import pymongo
import urllib
import datetime
import os

load_dotenv() #Load .env file
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB') #URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["website-class"] #Database name
collection = database["school-time-table"] #Collection school time table current
collection_archive = database["archive-school-time-table"] #Collection school time table archive

def update_time_school():
    # Load excel file
    namefile_xlsx = "attachments/school_time.xlsx"
    workbook = xl.load_workbook(filename=namefile_xlsx)
    date_style = NamedStyle(name='date_style',number_format='dd/mm/yy')
    workbook.add_named_style(date_style)
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
        "School Subject": {
            "Monday": [
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                      "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
            ],
            "Tuesday": [
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
            ],
            "Wednesday": [
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
            ],
            "Thursday": [
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
            ],
            "Friday": [
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
            ],
            "Saturday": [
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
                {
                    "Subject": "null",
                    "Teacher": "null",
                    "Room": "null",
                },
            ],
    }
}
    x = collection.delete_many({}) #Delete all documents in collection (school-time-table)
    x = collection.insert_one(mydict) # Add collection on collection (school-time-table)
    x = collection_archive.insert_one(mydict) # Add collection on collection (archive-school-time-table)
    check_repeat = 0
    check_repeat_teacher = 0
    check_repeat_room = 0
    dont_repeat = 0
    dont_repeat_teacher = 0
    dont_repeat_room = 0
    gagaga_teacher = 0
    gagaga_room = 0
    number_teacher = 1
    number_room = 1
    number = 1
    current_day = None
    day_counter = 0
    number_day = 0
    #Search my class in excel file and add in MongoDB
    number = 1
    gagaga = 0
    for row in range (1, 100):
        # column B ~ column F
        for column in range (1, 100):
            cell = ws.cell(row, column)
            if cell.value == "2elci":
                #Search school time table
                for i in range(4,80):
                    day = str(ws.cell(row=i, column=3).value) # Get day from excel file
                    school_subject = ws.cell(row=i, column=column).value # Get school subject from excel file
                    teacher = ws.cell(row=i, column=column+1).value
                    room = ws.cell(row=i, column=column+2).value
                    if dont_repeat == 9:
                        check_repeat += 1
                        if check_repeat == 5:
                            check_repeat = 0
                            dont_repeat = 0
                    else:
                        if day == "None":
                            if school_subject == 0: #If school subject is 0, add "null" in MongoDB
                                number += 1
                                gagaga += 1
                                dont_repeat += 1
                                if number == 9:
                                    number = 1
                                if gagaga == 9:
                                    gagaga = 0
                            else: #If school subject is not 0, add school subject in MongoDB
                                #remove_things_in_front = school_subject.split(' ', 1)[1]
                                find_document_school_time_table = list(collection.find({}, {"Date": long_date}))
                                find_document_archive_school_time_table = list(collection_archive.find({}, {"Date": long_date}))
                                array_document_school_time_table = find_document_school_time_table[0]["_id"]
                                array_document_archive_school_time_table = find_document_archive_school_time_table[0]["_id"]
                                # Add school subject in MongoDB beacause school subject is not 0
                                collection.update_one(
                                    { "_id": ObjectId(array_document_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga) + ".Subject": school_subject,
                                    }
                                }
                            )
                                collection_archive.update_one(
                                    { "_id": ObjectId(array_document_archive_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga) + ".Subject": school_subject,
                                    }
                                }
                            )
                                number += 1
                                gagaga += 1
                                dont_repeat += 1
                                if number == 9:
                                    number = 1
                                if gagaga == 8:
                                    gagaga = 0
                        else:
                            datetime_obj = datetime.datetime.strptime(day, "%Y-%m-%d %H:%M:%S").strftime("%d %m %Y")
                            convert_date_to_day = datetime.datetime.strptime(datetime_obj, '%d %m %Y').strftime('%A')
                            array_test = []
                            array_test.append(convert_date_to_day)
                            number_day += 1
                            if school_subject == 0: #If school subject is 0, add "null" in MongoDB
                                find_document_school_time_table = list(collection.find({}, {"Date": long_date}))
                                find_document_archive_school_time_table = list(collection_archive.find({}, {"Date": long_date}))
                                array_document_school_time_table = find_document_school_time_table[0]["_id"]
                                array_document_archive_school_time_table = find_document_archive_school_time_table[0]["_id"]
                                collection.update_one(
                                    { "_id": ObjectId(array_document_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga) + ".Subject": school_subject,
                                    }
                                }
                            )
                                collection_archive.update_one(
                                    { "_id": ObjectId(array_document_archive_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga) + ".Subject": school_subject,
                                    }
                                }
                            )

                                number += 1
                                gagaga += 1
                                dont_repeat += 1
                                number = 0
                                if number == 9:
                                    number = 1
                                if gagaga == 8:
                                    gagaga = 0
                            else: #If school subject is not 0, add school subject in MongoDB
                                #remove_things_in_front = school_subject.split(' ', 1)[1]
                                find_document_school_time_table = list(collection.find({}, {"Date": long_date}))
                                find_document_archive_school_time_table = list(collection_archive.find({}, {"Date": long_date}))
                                array_document_school_time_table = find_document_school_time_table[0]["_id"]
                                array_document_archive_school_time_table = find_document_archive_school_time_table[0]["_id"]
                                # Add school subject in MongoDB beacause school subject is not 0
                                collection.update_one(
                                    { "_id": ObjectId(array_document_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga)+ ".Subject": school_subject,
                                    }
                                }
                            )
                                collection_archive.update_one(
                                    { "_id": ObjectId(array_document_archive_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga)+ ".Subject": school_subject,
                                    }
                                }
                            )
                                number += 1
                                gagaga += 1
                                dont_repeat += 1
                                if number == 9:
                                    number = 1
                                if gagaga == 8:
                                    gagaga = 0

                    #Search teacher
                    if dont_repeat_teacher == 9:
                        check_repeat_teacher += 1 # 13
                        if check_repeat_teacher == 5:
                            check_repeat_teacher = 0
                            dont_repeat_teacher = 0
                            #number = 1
                    else:
                        if day == "None":
                            if teacher == 0:
                                number_teacher += 1
                                gagaga_teacher += 1
                                dont_repeat_teacher += 1
                                if number_teacher == 9:
                                    number_teacher = 1
                                if gagaga_teacher == 9:
                                    gagaga_teacher = 0
                            else:
                                find_document_school_time_table = list(collection.find({}, {"Date": long_date}))
                                find_document_archive_school_time_table = list(collection_archive.find({}, {"Date": long_date}))
                                array_document_school_time_table = find_document_school_time_table[0]["_id"]
                                array_document_archive_school_time_table = find_document_archive_school_time_table[0]["_id"]
                                collection.update_one(
                                    { "_id": ObjectId(array_document_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga_teacher) + ".Teacher": teacher,
                                    }
                                }
                            )
                                collection_archive.update_one(
                                    { "_id": ObjectId(array_document_archive_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga_teacher)+ ".Teacher": teacher,
                                    }
                                }
                            )
                                number_teacher += 1
                                gagaga_teacher += 1
                                dont_repeat_teacher += 1
                                if number_teacher == 9:
                                    number_teacher = 1
                                if gagaga_teacher == 8:
                                    gagaga_teacher = 0
                        else:
                            datetime_obj = datetime.datetime.strptime(day, "%Y-%m-%d %H:%M:%S").strftime("%d %m %Y")
                            convert_date_to_day = datetime.datetime.strptime(datetime_obj, '%d %m %Y').strftime('%A')
                            array_test = []
                            array_test.append(convert_date_to_day)
                            find_document_school_time_table = list(collection.find({}, {"Date": long_date}))
                            find_document_archive_school_time_table = list(collection_archive.find({}, {"Date": long_date}))
                            array_document_school_time_table = find_document_school_time_table[0]["_id"]
                            array_document_archive_school_time_table = find_document_archive_school_time_table[0]["_id"]
                            collection.update_one(
                                        { "_id": ObjectId(array_document_school_time_table)},
                                        { "$set": {
                                            "School Subject." + array_test[0] + "." + str(gagaga_teacher)+ ".Teacher": teacher,
                                        }
                                    }
                                )
                            collection_archive.update_one(
                                    { "_id": ObjectId(array_document_archive_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga_teacher)+ ".Teacher": teacher,
                                    }
                                }
                            )
                            number_teacher += 1
                            gagaga_teacher += 1
                            dont_repeat_teacher += 1
                            if number_teacher == 9:
                                number_teacher = 1
                            if gagaga_teacher == 8:
                                gagaga_teacher = 0

                    #Search room school
                    if dont_repeat_room == 9:
                        check_repeat_room += 1
                        if check_repeat_room == 5:
                            check_repeat_room = 0
                            dont_repeat_room = 0
                    else:
                        if day == "None":
                            if room == 0:
                                number_room += 1
                                gagaga_room += 1
                                dont_repeat_room += 1
                                if number_room == 9:
                                    number_room = 1
                                if gagaga_room == 9:
                                    gagaga_room = 0
                            else:
                                find_document_school_time_table = list(collection.find({}, {"Date": long_date}))
                                find_document_archive_school_time_table = list(collection_archive.find({}, {"Date": long_date}))
                                array_document_school_time_table = find_document_school_time_table[0]["_id"]
                                array_document_archive_school_time_table = find_document_archive_school_time_table[0]["_id"]
                                collection.update_one(
                                    { "_id": ObjectId(array_document_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga_room) + ".Room": room,
                                    }
                                }
                            )
                                collection_archive.update_one(
                                    { "_id": ObjectId(array_document_archive_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga_room)+ ".Room": room,
                                    }
                                }
                            )
                                number_room += 1
                                gagaga_room += 1
                                dont_repeat_room += 1
                                if number_room == 9:
                                    number_room = 1
                                if gagaga_room == 8:
                                    gagaga_room = 0
                        else:
                            datetime_obj = datetime.datetime.strptime(day, "%Y-%m-%d %H:%M:%S").strftime("%d %m %Y")
                            convert_date_to_day = datetime.datetime.strptime(datetime_obj, '%d %m %Y').strftime('%A')
                            array_test = []
                            array_test.append(convert_date_to_day)
                            find_document_school_time_table = list(collection.find({}, {"Date": long_date}))
                            find_document_archive_school_time_table = list(collection_archive.find({}, {"Date": long_date}))
                            array_document_school_time_table = find_document_school_time_table[0]["_id"]
                            array_document_archive_school_time_table = find_document_archive_school_time_table[0]["_id"]
                            collection.update_one(
                                        { "_id": ObjectId(array_document_school_time_table)},
                                        { "$set": {
                                            "School Subject." + array_test[0] + "." + str(gagaga_room)+ ".Room": room,
                                        }
                                    }
                                )
                            collection_archive.update_one(
                                    { "_id": ObjectId(array_document_archive_school_time_table)},
                                    { "$set": {
                                        "School Subject." + array_test[0] + "." + str(gagaga_room)+ ".Room": room,
                                    }
                                }
                            )
                            number_room += 1
                            gagaga_room += 1
                            dont_repeat_room += 1
                            if number_room == 9:
                                number_room = 1
                            if gagaga_room == 8:
                                gagaga_room = 0

update_time_school()