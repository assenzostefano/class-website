from dotenv import load_dotenv
from bson.objectid import ObjectId

from discord.ext import tasks, commands
import discord
import pymongo
import urllib.parse
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

bot = discord.Bot()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    bot.loop.create_task(orario())

@tasks.loop(seconds=1)
async def orario():
    documents = collection.find()

# Iterate through the documents
    for document in documents:
        for day in document['School Subject']:
            for i, subject in enumerate(document['School Subject'][day]):
                if subject['Subject'] == "CALF1 LINGUA ITALIANA":
                    channel = bot.get_channel(1063753802638954519)
                    #await ctx.send(f"Subject found: {subject['Subject']} at index: {i}")
                    await channel.send(f"Hours school: {i}, Subject: {subject['Subject']}, Teacher: {subject['Teacher']}, Room: {subject['Room']}")

bot.run(DISCORD_TOKEN)