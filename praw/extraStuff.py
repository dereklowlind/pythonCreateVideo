# top level comments
submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print("author=" + str(top_level_comment.author))
    print(top_level_comment.body)
    if top_level_comment.replies:
        print("    " + str(top_level_comment.replies[0].author))
        print("    " + str(top_level_comment.replies[0].body))

    print()
    print()

# TODO figure out what level a comment is at
# all comments
# submission.comments.replace_more(limit=0)
# for comment in submission.comments.list():
#     print(comment.author)
#     print(comment.body)
#     print()
#     print()

    #  loop through sub comments
    getSubComments(tlc, level, commentsData)
    # comment = tlc
    # if comment.replies:
    #     level += 1 # increment the comment level
    #     for subcomment in comment.replies:
    #         commentsData.append([subcomment.author, subcomment.body, level])
