from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def website():
    return render_template("index.html")

@app.route("/recommendations")
def recommended():
    description = request.args.get('description')
    return render_template("recommendations.html", description=description)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5400")