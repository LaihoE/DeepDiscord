import speech_recognition as sr
from audiodownloader import download_video

def sr_api_call():
    recog = sr.Recognizer()
    text=""
    with sr.Microphone() as source:
        audio = recog.listen(source)
        try:
            text = recog.recognize_google(audio)
            print(text)
        except:
            print('Error on googleEARS')
        if text != "":
            download_video(text)