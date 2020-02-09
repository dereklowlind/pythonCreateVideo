import json
from htmlToImage import createImages
from textToSpeech import createAudio
from generateClips import createClips

# open json
file_name = 'equ586.json'
directoryName = "data/" + file_name.split('.')[0]
json_file = open("data/" + file_name)
data = json.load(json_file)

print(directoryName)

# create images
createImages(data, directoryName)

# create audio
createAudio(data, directoryName)

# combine images and audio into video clips
createClips(data, directoryName)
# combine video clips