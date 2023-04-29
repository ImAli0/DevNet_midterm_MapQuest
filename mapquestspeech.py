# Import the required module for text
# to speech conversion
from gtts import gTTS
from chatgpt3api import response
from playsound import playsound
print(response)
# This module is imported so that we can

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=response, lang=language, slow=False)
# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted audio

playsound('welcome.mp3')