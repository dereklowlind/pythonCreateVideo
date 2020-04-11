import os 
import cv2 
from PIL import Image 
from mutagen.mp3 import MP3
import math

def createClip(imgFileName, audioFileName, videoFileName, ffmpeg_path): 
    frame = cv2.imread(imgFileName) 

    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape 
    videoFileNameNoAudio = videoFileName.split('.avi')[0] + 'NoAudio.avi'
    print("---- videoFileNameNoAudio", videoFileNameNoAudio)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(videoFileNameNoAudio, fourcc, 10, (width, height)) 

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
    cmd = ffmpeg_path + " -y -i " + videoFileNameNoAudio + " -i " + audioFileName + " -codec copy " + videoFileName
    os.system(cmd)


def createClips(data, directoryName, subId): 
    # make sure directory exists
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)
    ffmpeg_path = "ffmpeg"
    isWindows = False
    if os.name == 'nt':
        ffmpeg_path = '.\\packages\\windows\\ffmpeg-20200213-6d37ca8-win64-static\\ffmpeg-20200213-6d37ca8-win64-static\\bin\\ffmpeg.exe'
        isWindows = True
    # make sure final_video directory exists
    # directoryName points to ./data/<reddit_id>
    final_videos_dir = directoryName + '/../../final_videos'
    if not os.path.exists(final_videos_dir):
        os.makedirs(final_videos_dir)
    
    currDir = os.getcwd()

    # for submission
    imgFileName = "./" + directoryName + "/submission" + ".jpg"
    audioFileName = "./" + directoryName + "/submission" + ".mp3"
    videoFileName = "./" + directoryName + "/submission" + ".avi"
    createClip(imgFileName, audioFileName, videoFileName, ffmpeg_path)
    if isWindows:
        concatFiles = "file '" + currDir + "\\" + directoryName + "\\submission" + ".avi" + "'"
    else:
        concatFiles = "file '" + currDir + "/" + directoryName + "/submission" + ".avi" + "'"
    # for comments
    com=data["commentsData"]
    for i in range(len(com)):
        if com[i]["isChecked"]:
            imgFileName = "./" + directoryName + "/" + str(i) + ".jpg"
            audioFileName = "./" + directoryName + "/" + str(i) + ".mp3"
            videoFileName = "./" + directoryName + "/" + str(i) + ".avi"
            createClip(imgFileName, audioFileName, videoFileName, ffmpeg_path)
            if isWindows:
                concatFiles += ("\nfile '" + currDir + "\\" + directoryName + "\\" + str(i) + ".avi" + "'")
            else:
                concatFiles += ("\nfile '" + currDir + "/" + directoryName + "/" + str(i) + ".avi" + "'")
    
    # concatenate clips together
    toConcatFile = directoryName + "/toConcat.txt"
    f = open(toConcatFile, "w")
    f.write(concatFiles)
    f.close()
    finalName = "./final_videos/" + subId + ".avi"
    if isWindows:
        toConcatFile = toConcatFile.replace("/", "\\")
    concatCMD = ffmpeg_path + " -y -f concat -safe 0 -i " + toConcatFile + " -c copy " + finalName
    os.system(concatCMD)
    print(concatCMD)