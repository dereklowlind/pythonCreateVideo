# https://pypi.org/project/imgkit/
import imgkit
import os

currentDir = os.getcwd() + "/"
header='<html><body>'
footer='</body></html>'
css='''<link rel="stylesheet" href="''' + currentDir +  "test2.css" + '''">'''



def subHTML(subAuthor, subBody, subScore):
    subHTML = header + css + '''
        <div class="flex-container">
            <div class="arrows-and-line"> 
                <img src="''' + currentDir + "reddit-uparrow.png" + '''" class="votearrow"/>
                <a class="scorestyle">''' + subScore + '''</a>
                <img src="''' + currentDir + "reddit-downarrow.png" + '''" class="votearrow"/>
            </div>
            <div>
                <a class="subAuthorstyle">Posted by u/'''+ subAuthor +'''</a>
                <p class="paragraphstyle">''' + subBody + '''</p>
            </div>
            </div>
    ''' + footer
    return subHTML


def comHTML(entryAuthor, entryBody, level):
    extraLevelTabs = '<div class="linestyle"></div>' * (level -1)
    commentHTML= header + css + '''
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
    ''' + footer
    return commentHTML


# test data
subAuthor = "mto96"
subBody = '''Check out this talk from GOTO Copenhagen 2019 by Roy Osherove, author of "The Art Of Unit Testing" and "Elastic Leadership.Growing self-organizing teams". You can find the link to the talk, along with the full talk abstract pasted below: [https://youtu.be/goihWvyqRow?list=PLEx5khR4g7PLHBVGOjNbevChU9DOL3Axj](https://youtu.be/goihWvyqRow?list=PLEx5khR4g7PLHBVGOjNbevChU9DOL3Axj) They say that "you get what you measure", and we've all seen it happen. "We need to get the coverage up!" followed by people frantically writing tests that might not actually test anything. Coverage is up. Quality? Not so much. So what metrics can we use to drive the things we believe in? In this session Roy Osherove covers recommended and un-recommended metrics and how each one could drive our team towards a bleaker, or brighter future. **What will the audience learn from this talk?** * Leading vs lagging indicators and their value * What metrics can hurt your agility * What metrics push towards agility * Influence forces and why people behave in specific ways (and how metrics play a role)'''
subScore = "56"

entryAuthor = "sunzoo"
entryBody = '''Code coverage in particular is an interesting metric. There was a paper floating
                around from Microsoft that found that having good code coverage didn't mean indicate low defects, but not having
                it indicated bad code. Not the best metric to track, but still valuable in the must be this tall to enter sense.
            '''
level = 3
make =  comHTML(entryAuthor, entryBody, 2) + "<a>hello!</a>" 
print(make)

# subHTML(subAuthor,subBody,subScore)

imgkit.from_string(make, 'out.jpg')
# imgkit.from_file('test3.html', 'out3.jpg')

