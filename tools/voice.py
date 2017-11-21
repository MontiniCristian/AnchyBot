from gtts import gTTS
import time

now = time.strftime("%c")


def Voicer(msg):
    """
    This function take a string as single arg and convert in to voice.
    Return the path of the saved '.mp3'
    :param msg:
    :return String --> The path of '.mp3' file:
    """

    now = time.strftime("%c")
    tts = gTTS(text=str(msg), lang='en')
    tts.save('/home/debian/AnchyBot/Media/Audio/'+now + "_voice.mp3")
    return str('Media/Audio/'+now + "_voice.mp3")

