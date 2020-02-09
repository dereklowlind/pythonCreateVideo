import json
from htmlToImage import createImages
from textToSpeech import createAudio
from generateClips import createClips
import time

start_time = time.time()

# open json
file_name = 'esr647.json'
directoryName = "data/" + file_name.split('.')[0]
json_file = open("jsons/" + file_name)
data = json.load(json_file)

print(directoryName)

# create images
createImages(data, directoryName)

# create audio
# createAudio(data, directoryName)

# combine images and audio into video clips
createClips(data, directoryName, file_name.split('.')[0])

total_time = time.time() - start_time
minutes = int(total_time/60)
seconds = int(total_time%60)
print("My program took", minutes, "minutes", seconds, "seconds", "to run")