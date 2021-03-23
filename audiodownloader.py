import requests
from music_player import stream_audio
from credentials import creds

def download_video(videoname):
    videoname.replace(' ','&')
    apikey=creds.google_api_key
    x=requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={videoname}&key={apikey}").json()
    vidid=x['items'][0]['id']['videoId']
    url='https://www.youtube.com/watch?v='+ vidid
    print(videoname)
    stream_audio(url,videoname)
