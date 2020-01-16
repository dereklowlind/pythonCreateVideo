# https://towardsdatascience.com/scraping-reddit-data-1c0af3040768


import praw
# from praw.models import MoreComments
import pandas as pd
import json

def getSubComments(comment, level, commentsData):
    if comment.replies:
        level += 1 # increment the comment level
        for subcomment in comment.replies:
            commentsData.append({"level":level, "author": str(subcomment.author), "body": str(subcomment.body), "isChecked": False})
            getSubComments(subcomment, level, commentsData)


url="https://www.reddit.com/r/devops/comments/elqkkg/what_metrics_can_we_use_to_drive_the_things_we/"

# setup reddit api client
reddit = praw.Reddit(client_id='QyfE0lzekE-wDQ', client_secret='ME3ZIEoH1aLaOt7NasRe_tJb20M', user_agent='videomaker')

submission = reddit.submission(url=url)
# submission = reddit.submission(id="a3p0uq")

# print(submission.author)
# print(submission.subreddit)
# print(submission.title)
# print(submission.selftext)
# print(submission.score)

submissionData = {
    "author": str(submission.author),
    "subreddit": str(submission.subreddit),
    "title": str(submission.title),
    "body": str(submission.selftext),
    "score": str(submission.score),
}
# subJson = json.dumps(submissionData)
# print(subJson)

# get comments with author and level
submission.comments.replace_more(limit=0)
commentsData = []
#tlc = top level comment
for tlc in submission.comments:
    level = 1
    commentsData.append({"level":level, "author": str(tlc.author), "body": str(tlc.body), "isChecked": False})

    #  loop through sub comments
    getSubComments(tlc, level, commentsData)

# commentsData=pd.DataFrame(commentsData, columns=['level', 'author', 'body'])
# commentJson = json.dumps(commentsData)
# print(commentJson[0])
# print(json.loads(commentJson)[2])

totalJson = {
    "submissionData": submissionData,
    "commentsData": commentsData
    }

with open("threadData.json", 'w') as f:
    json.dump(totalJson, f)
# print(totalJson)
