"""In a file called watch.py, implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value
of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL
will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain
no more than one such URL. If the input does not contain any such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import
any other libraries. You’re welcome, but not required, to use re and/or sys.
input example:
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
Because some HTML attributes are optional, you could instead minimally embed just the below.
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g., https://www.youtube.com/embed/xvFZjo5PgG0),
converting them back to shorter, shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.
"""

import re
import sys
PAT = r'<iframe .*src=\"http(s)?://(www\.)?youtube\.com/embed/(.*?)\".*></iframe>'
SHORT_PAT = 'https://youtu.be/'


def main():
    print(parse(input("HTML: ")))


def parse(s):
    res = re.search(PAT, s)
    if res:
        return SHORT_PAT + res.groups()[2]
    else:
        return None


if __name__ == "__main__":
    main()
