import re

def fix_string(data_str):

    data_vis = data_str.replace("fuck", "f**k")
    data_vis = data_vis.replace("dick", "d**k")

    data_speak = data_str.replace("fuck", "fk")
    data_speak = data_speak.replace("dick", "dk")
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