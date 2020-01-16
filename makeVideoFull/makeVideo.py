import json
from htmlToImage import createImages
from textToSpeech import createAudio
from generateClips import createClips

# open json
json_file = open('./myJSON.json')
data = json.load(json_file)
directoryName = 'aaaa'

# create images
# createImages(data, directoryName)

# create audio
# createAudio(data, directoryName)

# combine images and audio into video clips
createClips(data, directoryName)
# combine video clips