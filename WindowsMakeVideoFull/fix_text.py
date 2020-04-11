import re
import csv

def fix_string(data_str):
    f = open('word_replacement.csv', 'r')
    words_to_replace = csv.reader(f)
    next(words_to_replace)  # skip header row
    data_vis = data_str
    data_speak = data_str
    for word in words_to_replace:
        data_vis = data_vis.replace(word[0], word[1])
        data_speak = data_speak.replace(word[0], word[2])
    data_speak = re.sub(r"\(?http\S+\)?", "", data_speak)
    
    return [data_vis, data_speak]

# fix the weird unicode quotes and maybe later swearing
def fix_text(data):
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