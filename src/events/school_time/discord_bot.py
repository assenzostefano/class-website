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

@bot.slash_command(name="first_slash", guild_ids=['1063753799874912337']) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")

bot.run(DISCORD_TOKEN)