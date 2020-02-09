# https://pypi.org/project/imgkit/
import imgkit
import os
import json

currentDir = os.getcwd() + "/"
header='<html><body>'
footer='</body></html>'
css='''<link rel="stylesheet" href="''' + currentDir +  "htmlToImage.css" + '''">'''



def subHTML(subAuthor, subTitle, subScore):
    subHTML = header + css + '''
        <div class="flex-container">
            <div class="arrows-and-line"> 
                <img src="''' + currentDir + "reddit-uparrow.png" + '''" class="votearrow"/>
                <a class="scorestyle">''' + subScore + '''</a>
                <img src="''' + currentDir + "reddit-downarrow.png" + '''" class="votearrow"/>
            </div>
            <div>
                <a class="subAuthorstyle">Posted by u/'''+ subAuthor +'''</a>
                <p class="subTitlesyle">''' + subTitle + '''</p>
            </div>
            </div>
    ''' + footer
    return subHTML


def comHTML(entryAuthor, entryBody, level):
    extraLevelTabs = '<div class="linestyle"></div>' * (level -1)
    commentHTML= '''
        <div>
        <div class="flex-container">
        ''' + extraLevelTabs + '''
            <div class="arrows-and-line">
                <img src="''' + currentDir + "reddit-uparrow.png" + '''" class="votearrow"/>
                <img src="''' + currentDir + "reddit-downarrow.png" + '''" class="votearrow"/>
                <div class="linestyle"></div>
            </div>
            <div>
                <a class="comAuthorstyle">'''+ entryAuthor +'''</a>
                <p class="paragraphstyle">'''+ entryBody +''' </p>
            </div>
        </div>
        <div>
    '''
    return commentHTML


def createSubmissionImage(sub, directoryName):
    fileName = "./" + directoryName + "/submission.jpg"
    subScoreInt = int(sub["score"])
    subScoreStr = sub["score"]
    if subScoreInt >= 1000:
        subScoreInt = format((subScoreInt/1000), '.1f')
        subScoreStr = str(subScoreInt) +"K"
    make = subHTML(sub["author"],sub["title"],subScoreStr)
    imgkit.from_string(make, fileName)

def createCommentImages(com, directoryName):
    for i in range(len(com)):
        if com[i]["isChecked"]:
            fileName = "./" + directoryName + "/" + str(i) + ".jpg"
            if com[i]["level"] > 1:
                make = header + css 
                start = i - com[i]["level"] + 1
                end = i + 1 # so range hits i
                for j in range(start, end):
                    make += comHTML(com[j]["author"],com[j]["body"],com[j]["level"])  
                make += footer
            else:
                make = header + css + comHTML(com[i]["author"],com[i]["body"],com[i]["level"])  + footer
            imgkit.from_string(make, fileName)

def fix_string(data_str):
    # fix the unicode quote
    data_str = data_str.replace("’", "'")
    data_str = data_str.replace("‘", "'")
    data_str = data_str.decode('utf-8','ignore').encode("utf-8")
    return data_str

# fix the weird unicode quotes and maybe later swearing
def fix_data(data):
    data["submissionData"]["title"] = fix_string(data["submissionData"]["title"])
    data["submissionData"]["body"] = fix_string(data["submissionData"]["body"])
    for com in data["commentsData"]:
        com["body"] = fix_string(com["body"])
    return data
def createImages(data, directoryName):
    data_fixed = fix_data(data)
    # make sure directory exists
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)
    # create submission image
    createSubmissionImage(data["submissionData"], directoryName)
    # create comment images
    createCommentImages(data["commentsData"], directoryName)
    

