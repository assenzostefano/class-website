from commands.moderation import ban, kick, clear_msg
from discord.commands.context import ApplicationContext # Discord
from selenium.webdriver.firefox.options import Options # Selenium
from discord.commands import Option # Discord
from discord.ext import commands
from bson.objectid import ObjectId # MongoDB
from selenium import webdriver # Selenium
from dotenv import load_dotenv 
from selenium import webdriver # Selenium
from discord.ext import tasks # Discord
import urllib.parse # MongoDB
import datetime # Date
import discord # Discord
import pymongo # MongoDB
import time # Time
import os # OS

# .env
load_dotenv()  # Load .env file
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')  # Discord token
GENERAL_ID = os.getenv('GENERAL_ID')  # Channel ID
PASSWORD_MONGODB = os.getenv('PASSWORD_MONGODB')  # Password for MongoDB
URL_MONGODB = os.getenv('URL_MONGODB')  # URL for MongoDB

# MongoDB
mongo_url = "mongodb+srv://elci:" + urllib.parse.quote_plus(PASSWORD_MONGODB) + URL_MONGODB  # URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url)  # Connect to MongoDB
database = client["website-class"]  # Database name
collection = database["school-time-table"] # Collection school time table current
collection_email = database["email"]  # Collection email

#Date
current_time = datetime.datetime.now() # Current time
day = str(current_time.day) # Day
month = str(current_time.month) # Month
year = str(current_time.year) # Year
hour = str(current_time.hour) # Hour
minute = str(current_time.minute) # Minute
long_date = day + "-" + month + "-" + year + " " + hour + ":" + minute # Long date with day, month, year, hour and minute

bot = discord.Bot()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    bot.loop.create_task(orario())

# Search on MongoDB the subject and send a message on Discord if the subject is found
@tasks.loop(seconds=1)
async def orario():
    documents = collection.find()
    send_screenshot = 0

    # Iterate through the documents
    for document in documents:
        for day in document['School Subject']:
            for i, subject in enumerate(document['School Subject'][day]):
                if subject['Subject'] == "CALF1 LINGUA ITALIANA":
                    # Send a message on channel #general with the subject found and the index of the subject
                    options = Options() # Set options
                    options.add_argument("--headless") # Headless mode (so you don't see the browser)
                    options.add_argument('--disable-gpu') # Disable GPU
                    if send_screenshot == 0:
                        driver = webdriver.Firefox(options=options)
                        driver.get('http://127.0.0.1:4999/orario')
                        time.sleep(5)

                        driver.get_screenshot_as_file("screenshot.png")
                        driver.quit()
                        channel = bot.get_channel(GENERAL_ID)
                        await channel.send(file=discord.File("screenshot.png"))
                        os.remove("screenshot.png")
                        send_screenshot += 1
                    else:
                        pass
                    channel = bot.get_channel(GENERAL_ID)
                    await channel.send(f"Day: {day}, Hour school: {i}, Subject found: {subject['Subject']} at index: {i}")
    send_screenshot = 0


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
                    choices=["First hour", "Second hour", "Third hour", "Fourth hour", "Fifth hour", "Sixth hour", "Seventh hour", "Eighth hour", "Ninth hour"],
                    required=True,
                    ), text: str,
    teacher: Option(str,
                    "Write teacher",
                    required=False,
    ),
    room: Option(str,
                    "Write room school",
                    required=False,
    ),
):
    
    await ctx.respond(f"Day selected: {day}, Hour school selected: {hour_school}, Text: {text}, Teacher: {teacher} ,Room: {room}")
    # Update the subject on MongoDB
    if hour_school == "First hour":
        hour_school = "0"
    elif hour_school == "Second hour":
        hour_school = "1"
    elif hour_school == "Third hour":
        hour_school = "2"
    elif hour_school == "Fourth hour":
        hour_school = "3"
    elif hour_school == "Fifth hour":
        hour_school = "4"
    elif hour_school == "Sixth hour":
        hour_school = "5"
    elif hour_school == "Seventh hour":
        hour_school = "6"
    elif hour_school == "Eighth hour":
        hour_school = "7"
    elif hour_school == "Ninth hour":
        hour_school = "8"

    find_document = list(collection.find({}, {"Date": long_date}))
    array_document = find_document[0]["_id"]
    collection.update_one(
        {"_id": ObjectId(array_document)},
        {"$set": {f"School Subject.{day}.{int(hour_school)}.Subject": text}}
    )

    if teacher != None:
        collection.update_one(
            {"_id": ObjectId(array_document)},
            {"$set": {f"School Subject.{day}.{int(hour_school)}.Teacher": teacher}}
        )

    if room != None:
        collection.update_one(
            {"_id": ObjectId(array_document)},
            {"$set": {f"School Subject.{day}.{int(hour_school)}.Room": room}}
        )

@bot.slash_command(name='confirm', description='Confirm change school time')
async def confirm(ctx : ApplicationContext):
    await ctx.respond(f"Confirm")
    collection_email.update_one({}, {"$set": {"Send on Whatsapp": "yes"}})
#@bot.slash_command()
#@discord.default_permissions(ban_members = True, administrator = True)
#async def ban(ctx, member: Option(discord.Member, description="Select a member", required=True), reason: Option(str, description="Reason", required=True)):
#    ban.ban_user(bot, ctx, member, reason)
#
#@bot.slash_command()
#@discord.default_permissions(kick_members = True, administrator = True)
#async def kick(ctx, member: Option(discord.Member, description="Select a member", required=True), reason: Option(str, description="Reason", required=True)):
#    kick.kick_user(bot, ctx, member, reason)
#
#@bot.slash_command(name= 'clear', description= 'Clears messages from a channel')
#@commands.has_permissions(manage_messages=True, administrator=True)
#@commands.cooldown(1, 5, commands.BucketType.user)
#async def clear(ctx, messages: Option(int, description="Amount of messages to delete", required=True)):
#    clear_msg.clear_messages(ctx, amount = messages)

bot.run(DISCORD_TOKEN)