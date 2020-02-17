"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from gtts import gTTS
import os

def callAudio(text, fileName):
    # synthesis_input = texttospeech.types.SynthesisInput(text=text)
    tts = gTTS(text=text, lang='en')

    with open(fileName, 'wb') as out:
        # Write the response to the output file.
        tts.write_to_fp(out)
        # out.write(response.audio_content)
        print('Audio content written to file ' + fileName)

def createAudio(data, directoryName):
    # make sure directory exists
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)
    # create submission audio
    callAudio(data["submissionData"]["title_speak"], directoryName+"/submission.mp3")
    
    # create comment audio
    com = data["commentsData"]
    for i in range(len(com)):
        if com[i]["isChecked"]:
            fileName = "./" + directoryName + "/" + str(i) + ".mp3"
            callAudio(com[i]["body_speak"], fileName)
    
