**SmartDiscordBot**

A bot that currently has the following capabilities

**Speech to text**
  * Can play youtube videos with voice commands

**Question and answering**
  * The bot is able to answer question based on a text the user gives the bot.
![alt text](https://github.com/LaihoE/DeepDiscord/blob/master/pics/fixedpic.png?raw=true)

**Setting up**

Before using the speech to text capabilities you need to download the deepspeech models by using the following commands:

```
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```
Then move the two files into the 'deepspeech' folder.

Finally you need to get an API key from google, get a discord token and the IDs of your discord channels. These should be put in 'credentials.py'.

**Using the bot**

for speech to text run **main.py**

for Q&A run **QandA.py**
