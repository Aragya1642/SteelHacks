from flask import Flask, request, jsonify, make_response
import getStuff
from flask_cors import CORS, cross_origin
import logging
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

logger = logging.getLogger(__name__)
#interests
#get data from website and feed
#get 
@app.route("/")
@cross_origin()
def test():
    return "Hello World"

def getDescription(method):
    if method=='POST':
        logger.debug("This is a post")
        logger.debug(request.form)
        description = request.form.get('description')
    else:
        logger.debug("This is a get")
        logger.debug(request.args)
        description = request.args.get('description')
    return description

@app.route("/getCalendarEvents", methods = ['GET', 'POST'])
@cross_origin()
def getEvents():
    logger.debug("Getting Calendar Events")
    description = getDescription(request.method)
    events = getStuff.getEvents(description, "bb_output.json", "full_output.json")
    urls = []
    for i in events:
        urls.append(i['event']['url']+".ics")
    return urls

@app.route("/getObjects", methods = ['GET', 'POST'])
@cross_origin()
def getObjects():
    print("here")
    logger.debug("Getting Objects")
    description = getDescription(request.method)
    print(description)
    stuff = getStuff.getEvents(description, "bb_output.json", "full_output.json")
    print(jsonify(stuff).status)
    return make_response(jsonify(data=stuff, mimetype='application/json'))

@app.route("/getTitles", methods = ['GET', 'POST'])
@cross_origin()
def getTitles():
    logger.debug("Getting Titles")
    description = getDescription(request.method)
    events = getStuff.getEvents(description, "bb_output.json", "full_output.json")
    titles = []
    for i in events:
        titles.append(i['event']['title'])
    return titles

if __name__=='__main__':
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    app.run('0.0.0.0', debug=True)
    logger.info("App started")
