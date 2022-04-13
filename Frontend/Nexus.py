from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import globals

app = Flask(__name__)
app.config['RIOT_API_KEY'] = 'RGAPI-e9b2b885-07ce-4637-904e-4dd3e208fc90'
globals.init()


# Defining routes for the site, directing the user to the desired page
@app.route("/logoclick", methods=["POST", "GET"])
def logoclick():
    return render_template("index.html")


@app.route("/", methods=["POST", "GET"])
def default():
    return render_template("index.html")


@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/champions", methods=["POST", "GET"])
def champions():
    return render_template("champions.html")


@app.route("/lookup", methods=["POST", "GET"])
def lookup():
    if request.method == "POST":
        summoner = request.form["nm"]
        return redirect(url_for("datadisplay", summoner=summoner))
    else:
        return render_template("summonersearch.html")


@app.route("/display/<summoner>", methods=["POST", "GET"])
def datadisplay(summoner):
    return render_template("dataDisplay.html")


@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("aboutus.html")


@app.route("/support", methods=["POST", "GET"])
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)
