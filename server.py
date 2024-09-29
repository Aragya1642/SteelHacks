from flask import Flask, request

app = Flask(__name__)

#interests
#get data from website and feed
#get 
@app.route("/")
def test():
    return "Hello World"

@app.route("/getEvents/<description>")
def getEvents():
    file = open("bb_output.json", "r")
    description = request.args.get('description')
    print("here")
    return "here"


if __name__=='__main__':
    app.run()
