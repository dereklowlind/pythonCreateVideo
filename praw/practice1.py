# https://towardsdatascience.com/scraping-reddit-data-1c0af3040768


import praw
from praw.models import MoreComments
import pandas as pd

reddit = praw.Reddit(client_id='QyfE0lzekE-wDQ', client_secret='ME3ZIEoH1aLaOt7NasRe_tJb20M', user_agent='videomaker')

# # get 10 hot posts from the MachineLearning subreddit
# hot_posts = reddit.subreddit('All').hot(limit=10)
# for post in hot_posts:
#     print(post.title)


# posts = []
# ml_subreddit = reddit.subreddit('MachineLearning')
# for post in ml_subreddit.hot(limit=10):
#     posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
# posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
# print(posts)



# # get MachineLearning subreddit data
# ml_subreddit = reddit.subreddit('MachineLearning')
# print(ml_subreddit.description)

# submission = reddit.submission(url="https://www.reddit.com/r/MapPorn/comments/a3p0uq/an_image_of_gps_tracking_of_multiple_wolves_in/")
# or 
submission = reddit.submission(id="a3p0uq")

# for top_level_comment in submission.comments:
#     if isinstance(top_level_comment, MoreComments):
#         continue
#     print(top_level_comment.body)


# top level comments
# submission.comments.replace_more(limit=0)
# for top_level_comment in submission.comments:
#     print(top_level_comment.body)


# all comments
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    print(comment.body)