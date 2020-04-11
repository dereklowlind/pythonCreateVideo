import json
from htmlToImageMulti import createImages
from gcloudTextToSpeech import createAudio # multi doesn't work probably due to credentials
from generateClipsMulti import createClips
import time
import re
import os

def fix_string(data_str):
    # fix the unicode quote

    data_vis = data_str.replace("fuck", "f**k")
    data_vis = data_vis.replace("dick", "d**k")

    data_speak = data_str.replace("fuck", "fk")
    data_speak = data_speak.replace("dick", "dk")
    data_speak = re.sub(r"\(?http\S+\)?", "", data_speak)
    
    return [data_vis, data_speak]

# fix the weird unicode quotes and maybe later swearing
def fix_data(data):
    data_vis, data_speak = fix_string(data["submissionData"]["title"])
    data["submissionData"]["title_vis"] = data_vis
    data["submissionData"]["title_speak"] = data_speak
    data_vis, data_speak = fix_string(data["submissionData"]["body"])
    data["submissionData"]["body_vis"] = data_vis
    data["submissionData"]["body_speak"] = data_speak
    for com in data["commentsData"]:
        data_vis, data_speak = fix_string(com["body"])
        com["body_vis"] = data_vis
        com["body_speak"] = data_speak
    return data



def process_file(file_name):
    start_time = time.time()
    # file_name = 'fv72ak.json'
    directoryName = "data/" + file_name.split('.')[0]
    json_file = open("jsons/" + file_name)
    data = json.load(json_file)

    print(directoryName)

    data = fix_data(data)
        
    # print(data)
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
    
    # Move a file by renaming it's path
    # move fron /jsons to /jsons/processed
    # os.rename("jsons/" + file_name, "jsons/processed/" + file_name)

# # get unprocessed jsons
# items = os.listdir("./jsons")
# newlist = []
# for names in items:
#     if names.endswith(".json"):
#         newlist.append(names)
# print(newlist)
# # ask user for (Y/n) confirmation
# val = input("Do you want to process these? (Y/n)")
# if val == 'Y':
#     for json_file in newlist:
#         process_file(json_file)

# process file and do not move it to processed
process_file('fv72ak.json')