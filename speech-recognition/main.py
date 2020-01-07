import speech_recognition as sr
import webbrowser
import os
import playsound
import random
import time

from gtts import gTTS

FUEGO_MUSIC = 'https://www.youtube.com/watch?v=ALoPRQFHaM4'
HRUSCA_MUSIC = 'https://www.youtube.com/watch?v=3GnP2qBBGqI'
FAVOURITE_MUSIC = 'https://www.youtube.com/watch?v=zX8-4H89Qzw'

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
        except sr.RequestError:
            print("Speech service si down.")
        return voice_data


def respond(voice_data):
    # print(voice_data)

    if 'holiday' in voice_data or 'Holiday' in voice_data:
        webbrowser.get().open(HRUSCA_MUSIC)

    if 'Fuego' in voice_data:
        webbrowser.get().open(FUEGO_MUSIC)

    if 'favourite' in voice_data:
        webbrowser.get().open(FAVOURITE_MUSIC)

    if 'exit' in voice_data or 'yes' in voice_data:
        exit(1)


def joker_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    rand = random.randint(1, 10000000)
    audio_file = 'audio-' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    # print(audio_string)
    os.remove(audio_file)


joker_speak('How can I help you?')
while 1:
    message = record_audio()
    respond(message)
    time.sleep(2)
    joker_speak('Is this ok?')
