from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import os
from asyncio import sleep
import sys
import pandas as pd
from credentials import creds

def stream_audio(url,videoname):
    token = creds.bot_token
    client = commands.Bot(command_prefix='.')
    print(creds.text_channel_id)
    @client.event
    async def on_ready():
        await client.get_channel(creds.text_channel_id).send(f"Playing {videoname}")
        vca = client.get_channel(creds.voice_channel_id)
        vc = await vca.connect()
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        if not vc.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
            vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            while vc.is_playing():
                await sleep(1)
            await client.close()
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            await client.get_channel(creds.text_channel_id).send("Already playing song")
            return

    @client.event
    async def on_message(message):
        if message.content == "!leave":
            await message.channel.send("Leaving")
            for vc in client.voice_clients:
                if vc.guild == message.guild:
                    await vc.disconnect()

    client.run(token)
