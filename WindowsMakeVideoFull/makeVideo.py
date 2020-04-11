import json
from htmlToImage import createImages
from gttsTextToSpeech import createAudio
from generateClips import createClips
from fix_text import fix_text
import time

start_time = time.time()

# open json
file_name = 'esr647.json'
directoryName = "data/" + file_name.split('.')[0]
json_file = open("jsons/" + file_name, encoding="utf8")
data = json.load(json_file)

print(directoryName)

data = fix_text(data)
print(data)

#create images
createImages(data, directoryName)

#create audio
createAudio(data, directoryName)

#combine images and audio into video clips
createClips(data, directoryName, file_name.split('.')[0])

total_time = time.time() - start_time
minutes = int(total_time/60)
seconds = int(total_time%60)
print("My program took", minutes, "minutes", seconds, "seconds", "to run")