
def AFK():
    import discord
    from discord.ext import tasks
    import time
    import random


    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            print('Message from {0.author}: {0.content}'.format(message))

            messageContent = message.content
            if len(messageContent) > 0:
                if "<@!375838524823306251>" in messageContent or "Salty" in messageContent or "salty" in messageContent or "rei" in messageContent or "Rei" in messageContent:
                    replies = ["whatchu want?",
                               "I'm afk",
                               "Stop spamming",
                               "Still afk",
                               "Master is currently afk, come back again later",
                               "Call me later ;3"]
                    await message.channel.send(random.choice(replies))
                    return

                if "sotty" in messageContent or "Sooty" in messageContent or "sooty" in messageContent or "nerd" in messageContent or "Nerd" in messageContent or "NERD" in messageContent:
                    replies = ["Sooty is still afk ;-;",
                               ";3 I'll be there soon loser~",
                               "Cominngg honeyyy gimme x minutes",
                               "waiitttt ahahhahaha",
                               "no u",
                               "angel =3="]
                    await message.channel.send(random.choice(replies))
                    return

                if messageContent == "s!back":
                    exit()


    client = MyClient()
    client.run('ODQ4OTAzNDMxNjIwMTMyODc0.YLTY7Q.BsgB87SN0nAlNQdfPrRtFu5ar9w')