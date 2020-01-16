import os 
import cv2 
from PIL import Image 
from mutagen.mp3 import MP3
import math

def createClip(imgFileName, audioFileName, videoFileName): 
    frame = cv2.imread(imgFileName) 

    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape 

    video = cv2.VideoWriter(videoFileName, 0, 10, (width, height)) 

    audioLength = MP3(audioFileName).info.length
    numSeconds = math.ceil(audioLength) * 10
    # print(audioLength)
    for i in range(numSeconds):
        # print(i)
        video.write(frame) 
    
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows() 
    video.release() # releasing the video generated 
    # add audio
    cmd = "ffmpeg -y -i " + videoFileName + " -i " + audioFileName + " -codec copy " + videoFileName
    os.system(cmd)


def createClips(data, directoryName): 
    # make sure directory exists
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)
    
    currDir = os.getcwd()

    # for submission
    imgFileName = "./" + directoryName + "/submission" + ".jpg"
    audioFileName = "./" + directoryName + "/submission" + ".mp3"
    videoFileName = "./" + directoryName + "/submission" + ".avi"
    # createClip(imgFileName, audioFileName, videoFileName)

    concatFiles = "file '" + currDir + "/" + directoryName + "/submission" + ".avi" + "'"
    # for comments
    com=data["commentsData"]
    for i in range(len(com)):
        if com[i]["isChecked"]:
            imgFileName = "./" + directoryName + "/" + str(i) + ".jpg"
            audioFileName = "./" + directoryName + "/" + str(i) + ".mp3"
            videoFileName = "./" + directoryName + "/" + str(i) + ".avi"
            # createClip(imgFileName, audioFileName, videoFileName)
            concatFiles += ("\nfile '" + currDir + "/" + directoryName + "/" + str(i) + ".avi" + "'")
    
    # concatenate clips together
    toConcatFile = directoryName + "/toConcat.txt"
    f = open(toConcatFile, "w")
    f.write(concatFiles)
    f.close()
    finalName = "./" + directoryName + "/final" + ".avi"
    concatCMD = "ffmpeg -y -f concat -safe 0 -i " + toConcatFile + " -c copy " + finalName
    # concatCMD = "ffmpeg -y -f concat -safe 0 -i " + toConcatFile + " -c copy " + finalName
    os.system(concatCMD)
    print(concatCMD)