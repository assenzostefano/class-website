from dotenv import load_dotenv
from bson.objectid import ObjectId

from discord.ext import tasks, commands
from discord.commands.context import ApplicationContext
from discord.commands import Option
import discord
import pymongo
import urllib.parse
import datetime
import os

load_dotenv()  # Load .env file
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')  # Discord token
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB')  # Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB')  # URL for MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB  # URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url)  # Connect to MongoDB
database = client["website-class"]  # Database name
# Collection school time table current
collection = database["school-time-table"]

#Date
current_time = datetime.datetime.now()
day = str(current_time.day)
month = str(current_time.month)
year = str(current_time.year)
hour = str(current_time.hour)
minute = str(current_time.minute)
long_date = day + "-" + month + "-" + year + " " + hour + ":" + minute

bot = discord.Bot()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    bot.loop.create_task(orario())

# Search on MongoDB the subject and send a message on Discord if the subject is found
@tasks.loop(seconds=1)
async def orario():
    documents = collection.find()

# Iterate through the documents
    for document in documents:
        for day in document['School Subject']:
            for i, subject in enumerate(document['School Subject'][day]):
                if subject['Subject'] == "CALF1 LINGUA ITALIANA":
                    # Send a message on channel #general with the subject found and the index of the subject
                    channel = bot.get_channel(1063753802638954519)
                    await channel.send(f"Day: {day}, Hour school: {i}, Subject found: {subject['Subject']} at index: {i}")

@bot.slash_command(name='change_school_time', description='Change school time')
async def change_school_time(
    ctx : ApplicationContext,
    day: Option(str,
                    "Select a day", 
                    choices=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], 
                    required=True,
                    ),
    hour_school: Option(str,
                    "Select hour school",
                    choices=["1", "2", "3", "4", "5", "6"],
                    required=True,
                    ), text: str
):
    
    await ctx.respond(f"Day selected: {day}, Hour school selected: {hour_school}, Text: {text}")
    # Update the subject on MongoDB
    find_document = list(collection.find({}, {"Date": long_date}))
    array_document = find_document[0]["_id"]
    collection.update_one(
        {"_id": ObjectId(array_document)},
        {"$set": {f"School Subject.{day}.{int(hour_school)}.Subject": text}}
    )

bot.run(DISCORD_TOKEN)