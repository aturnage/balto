import flask, flask.views
from flask import render_template
import urllib #importing to use its urlencode function
import urllib2 #for making http request
import json #for dedcoding a JSON response

app = flask.Flask(__name__)

api_key = "AIzaSyBVqyU6L4kGTMX6VHtQ9C19fM-tcWM0zkw"

searchTerm = raw_input("Search for a Ted talk video: ") #test in python
searchTerm = urllib.quote_plus(searchTerm + "ted talks") #hard coded ted talks in search

url ='https://www.googleapis.com/youtube/v3/search?part=snippet&q='+ searchTerm + '&key='+ api_key
response = urllib2.urlopen(url) #makes call to youtube
videos = json.load(response) #decodes the response to work with it

videoData = [] #declaring list

for video in videos['items']:
    if video['id']['kind'] == 'youtube#video':
        videoData.append(video['snippet']['title']+
        "\nhttp://youtube.com/watch?v="+video['id']['videoId']) #appends each video and title

videoData.sort(); #sorts alphabetically

print "\nSearch Results:\n"

for videoList in videoData:
    print videoList + "\n"

class View(flask.views.MethodView):
    def get(self):
        return "Well Hello there"

    @app.route('/')
    def render_static():
        return render_template('home.html')


app.add_url_rule('/', view_func=View.as_view('main'))
app.run()
