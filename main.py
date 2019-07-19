import modules
from flask import Flask

'''
PROJECT DETAILS : URL Shortener

URL Shortener reduces the characters or letters in a URL,
making them easier to read and remember.
A URL like xyz.com/wwryb78&svnhkn%sghq?sfiyh can be shortened to xyz.com/piojwr.

Examples of URL Shorteners

Here are some implementations of the URL Shortener idea:

    Bitly
    MeShort

Technical Details

The main objective of this project idea is to shorten URLs.
The main task the application will accomplish is to shorten URLs and
then redirect users to the original URL when the shortened URL is visited.

In the application, the users will input the original URL, and they will get the new, shortened URL as the result. To do this, you can use a combination of the random and string modules to generate the characters for the shortened URL.

Since users will visit the shortened URL days, months, or even years after,
you’ll need to save the original and shortened URLs in a database.
When a request comes in, the application checks if the URL exists and redirects to the original,
or else it redirects to a 404 page.

Extra Challenge

Generating a shortened URL with random characters makes for a better URL than the long, random ones.
But, you can make the result better for the users.
You can add a feature to customize URLs, so the users can customize the generated URLs themselves.

Without a doubt, a custom xyz.com/mysite URL is better than a randomly generated xyz.com/piojwr URL.
'''

originalUrl= input('Enter the url to shorten it : ')
app = Flask('__main__')

@app.route('/')
def hello_world():
    return 'Hello, World!'
