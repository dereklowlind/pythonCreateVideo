import praw
from flask import Flask, request, jsonify
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app)

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
    reddit = praw.Reddit(client_id='lFBsLCHPrHFysw', client_secret='21ykMnnDEFWTOUByvjRpZ_BKdZc', user_agent='gitpagesvideomaker')
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
    # print(totalJson)
    return totalJson

def getDataJSON(request):
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)
    
    request_json = request.get_json()
    if request.args and 'url' in request.args:
        response = jsonify(getDataStr(request.args.get('url')))
        response.headers.set('Access-Control-Allow-Origin', '*')
        response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
        return response
    elif request_json and 'url' in request_json:
        response = jsonify(getDataStr(request_json['url']))
        response.headers.set('Access-Control-Allow-Origin', '*')
        response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
        return response


# def getDataJSON():
#     request_json = request.get_json()
#     print("--url is: " + request_json.json['url'])
#     return jsonify(getDataStr(request_json.json['url']))

# curl -i -H "Content-Type: application/json" -X POST -d '{"url":"https://www.reddit.com/r/devops/comments/elqkkg/what_metrics_can_we_use_to_drive_the_things_we/"}' https://us-central1-pythonvideomaker.cloudfunctions.net/call-reddit-python
# {"url":"https://www.reddit.com/r/devops/comments/elqkkg/what_metrics_can_we_use_to_drive_the_things_we/"}
