import discord
from BERT import gobert
from credentials import creds
import os

token=creds.bot_token

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()
# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.

textfilepath=os.path.join(os.path.dirname(__file__),"Text_QnA","studytext.txt")

@bot.event
async def on_message(message):
    if "!study" in message.content:
        file=open(textfilepath,'w',encoding='UTF-8')
        file.write(message.content)
    if "!question" in message.content:
        question=message.content.replace('!question','')
        answer=gobert(question)
        await message.channel.send(answer)

bot.run(token)