import os
import discord
import csv
import random
from keep_alive import keep_alive

client = discord.Client()

VisitedLocations = []

def CleanString (originalString):
  characters_to_remove = "(),"

  new_string = originalString
  for character in characters_to_remove:
    new_string = new_string.replace(character, "")

  return new_string

def VisitedLocation (locationID):
  if locationID in VisitedLocations:
    result = True
  else:
    result = False
  return result

def CheckLocation(locationID):
  if locationID > 7:
    locationID = locationID - 7
  if VisitedLocation (locationID):
    locationID = CheckLocation(locationID+1)
    
  return locationID

@client.event
async def on_message(message):

  if message.author == client.user:
    return
  
  if message.content.startswith('$Quest'):
    with open('Metaplaces.txt', newline='') as f:
      reader = csv.reader(f)
      data = [tuple(row) for row in reader]

    NextLocation = 0
    result = "The Dweller on the Threshold guides your journey:\n"

    while NextLocation != 7:
      NextLocation = CheckLocation((random.randint(2,12) -1))
      VisitedLocations.append(NextLocation)
      result = result + "\n" + str((data[NextLocation]))

    await message.channel.send (CleanString(result))
    VisitedLocations.clear()




keep_alive()
client.run(os.environ['discordToken'])
