"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os

text = "2011 FERRARI 4 5 8 ITALIA. \
Doc Type: REBUILT SALVAGE.\
Odometer: 0 mi (NOT ACTUAL). \
Highlights: Enhanced Vehicles .\
Seller: State Farm Insurance.\
Primary Damage: front end.\
Secondary Damage: none.\
Estimated Retail Value:$187,000 .\
vin:ZFF67NFA8B0"

ssml = '<speak>2011 FERRARI <say-as interpret-as="characters">458</say-as> ITALIA <break strength="medium"/> \
Doc Type: REBUILT SALVAGE <break strength="weak"/>\
Odometer: 0 mi (NOT ACTUAL) <break strength="weak"/> \
Highlights: Enhanced Vehicle <break strength="weak"/>\
Seller: State Farm Insurance <break strength="weak"/>\
Primary Damage: front end <break strength="weak"/>\
Secondary Damage: none <break strength="weak"/>\
Estimated Retail Value:$187,000 <break strength="weak"/>\
vin:ZFF67NFA8B0 </speak>'

# Instantiates a client
os.environ ["GOOGLE_APPLICATION_CREDENTIALS"]= './testInterviewAudio-4a428f5a82cf.json'
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(ssml=ssml)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    name='en-US-Wavenet-A',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')