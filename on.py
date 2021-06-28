import discord
from discord.ext import tasks
import time
import random
from AFK_Replies import *
AFK()

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        messageContent = message.content


client = MyClient()
client.run('ODQ4OTAzNDMxNjIwMTMyODc0.YLTY7Q.BsgB87SN0nAlNQdfPrRtFu5ar9w')