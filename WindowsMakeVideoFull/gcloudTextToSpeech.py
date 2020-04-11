"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os



# Instantiates a client
os.environ ["GOOGLE_APPLICATION_CREDENTIALS"]= '/home/derek/D/testInterviewAudio-4a428f5a82cf.json'
client = texttospeech.TextToSpeechClient()

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    name='en-US-Wavenet-A',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)


def callAudio(text, fileName):
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=text)
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open(fileName, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
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
    
