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
mongo_url = "mongodb+srv://elci:" + \
    urllib.parse.quote_plus(PASSWORD_MONGODB) + \
    URL_MONGODB  # URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url)  # Connect to MongoDB
database = client["website-class"]  # Database name
# Collection school time table current
collection = database["school-time-table"]

bot = discord.Bot()


    
@tasks.loop(seconds=1)
async def orario(ctx):
    documents = collection.find()

# Iterate through the documents
    for document in documents:
        for day in document['School Subject']:
            for i, subject in enumerate(document['School Subject'][day]):
                if subject['Subject'] == "CALF1 LINGUA ITALIANA":
                    print(f"Subject found: {subject['Subject']} at index: {i}")
                    # Send a message on channel #general with the subject found and the index of the subject
                    channel = bot.get_channel(1063753802638954519).send("bot is online")
                    await ctx.send(f"Subject found: {subject['Subject']} at index: {i}")
    

@bot.command()
async def testpy(ctx):
    bot.loop.create_task(orario(ctx))
    await ctx.send("testpy")
bot.run(DISCORD_TOKEN)