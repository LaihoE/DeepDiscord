# Bot has the  following capabilities
**Speech to text**
  * Can play youtube videos with voice commands
  * Bot will make a beep sound when the wakeup word is recognized
  * After the beep say your song and the bot should join your channel with some music

**Question and answering**
  * The bot is able to answer questions based on a text the user gives the bot.
  * User inputs !study followed by text you want it to study
  * Then use !question followed by your question
  

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
