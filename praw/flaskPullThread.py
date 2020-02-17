# Flask==1.1.1
# praw==6.5.1

# https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

import praw
# from praw.models import MoreComments
import pandas as pd
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def getSubComments(comment, level, commentsData):
    if comment.replies:
        level += 1 # increment the comment level
        for subcomment in comment.replies:
            commentsData.append({"level":level, "author": str(subcomment.author), "body": str(subcomment.body), "isChecked": False, "score":str(subcomment.score)})
            getSubComments(subcomment, level, commentsData)

# example url
# url="https://www.reddit.com/r/devops/comments/elqkkg/what_metrics_can_we_use_to_drive_the_things_we/"

def getDataStr(url):
    # setup reddit api client
    reddit = praw.Reddit(client_id='QyfE0lzekE-wDQ', client_secret='ME3ZIEoH1aLaOt7NasRe_tJb20M', user_agent='videomaker')

    submission = reddit.submission(url=url)
    # submission = reddit.submission(id="a3p0uq")

    # subMissionId is used to name the JSON file and
    # the folder generated resources will be stored in
    subMissionId = str(submission.id)
    submissionData = {
        "author": str(submission.author),
        "subreddit": str(submission.subreddit),
        "title": str(submission.title),
        "body": str(submission.selftext),
        "score": str(submission.score),
    }

    # get comments with author and level
    submission.comments.replace_more(limit=0)
    commentsData = []
    #tlc = top level comment
    for tlc in submission.comments:
        level = 1
        commentsData.append({"level":level, "author": str(tlc.author), "body": str(tlc.body), "isChecked": False, "score":str(tlc.score)})

        #  loop through sub comments
        getSubComments(tlc, level, commentsData)

    totalJson = {
        "url": url,
        "id": subMissionId,
        "submissionData": submissionData,
        "commentsData": commentsData
        }
    print(totalJson)
    return totalJson

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/getdatajson', methods=['POST'])
def getDataJSON():
    print("--url is: " + request.json['url'])
    return jsonify(getDataStr(request.json['url']))

# curl -i -H "Content-Type: application/json" -X POST -d '{"url":"https://www.reddit.com/r/devops/comments/elqkkg/what_metrics_can_we_use_to_drive_the_things_we/"}' http://127.0.0.1:5000/getdatajson
# {"url":"https://www.reddit.com/r/devops/comments/elqkkg/what_metrics_can_we_use_to_drive_the_things_we/"}
if __name__ == '__main__':
    app.run()