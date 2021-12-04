import os
import discord
from dice import rollChummer
from keep_alive import keep_alive
from metaplane import AstralQuest

client = discord.Client()

@client.event
async def on_message(message):

  result = "Sorry chummer looks like something went wrong!"
  #Ignore own messages
  if message.author == client.user:
    return
  if message.content.startswith('$quest'):
    #Astral Quest message
    result = AstralQuest()    
  elif message.content.startswith('$roll'):
    #Dice roll
    result = rollChummer(message.content)
  elif message.content.startswith('$rad'):
    result = "Hoi there chummers, welcome to Rad' Shadowrunners shack\n"
    result+="Most of you meat sacks can't handle running in space so I'm creating a few programs to help you\n"
    result+="Meta Plane Journey planner\nJust type (yes type)\n   $quest\n"
    result+="Dice Roller type $roll <number of dice>,<target>,<reason your're doing this>\nIf you don't include a target it'll be an open roll, and reason is optional so all of these work:\n   $roll 5\n   $roll 5,4\n   $roll 5,Summmoning\n   $roll 5,4,Summoning\nYou can include spaces or not i dont care."

  await message.channel.send (result)
    
keep_alive()
client.run(os.environ['discordToken'])
