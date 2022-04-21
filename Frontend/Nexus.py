from flask import Flask, redirect, url_for, render_template, request
import riot_api
import globals
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///matches.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Set API key for function calls
app.config['RIOT_API_KEY'] = 'RGAPI-0ffe58eb-0746-422c-bb4c-b32eb7fdcdd4'
# Initialize Database
db = SQLAlchemy(app)


# Create Database Model
class Matches(db.Model):
    level_0 = db.Column(db.BIGINT, primary_key=True)
    level_1 = db.Column(db.BIGINT, primary_key=True)
    summonerName = db.Column(db.TEXT)
    summonerLevel = db.Column(db.BIGINT)
    champion = db.Column(db.BIGINT)
    championName = db.Column(db.TEXT)
    win = db.Column(db.BIGINT)
    kills = db.Column(db.BIGINT)
    deaths = db.Column(db.BIGINT)
    assists = db.Column(db.BIGINT)
    summoner1Id = db.Column(db.BIGINT)
    summoner2Id = db.Column(db.BIGINT)
    item1 = db.Column(db.BIGINT)
    item2 = db.Column(db.BIGINT)
    item3 = db.Column(db.BIGINT)
    item4 = db.Column(db.BIGINT)
    item5 = db.Column(db.BIGINT)
    item6 = db.Column(db.BIGINT)
    totalMinionsKilled = db.Column(db.Integer)
    visionWardsBoughtInGame = db.Column(db.Integer)
    visionScore = db.Column(db.Integer)
    totalDamageDealt = db.Column(db.BIGINT)
    totalDamageDealtToChampions = db.Column(db.BIGINT)

    __table_args__ = (
        db.PrimaryKeyConstraint("level_0", "level_1"),
    )


# Create Database
db.drop_all()
db.create_all()

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
    riot_api.data_fetch(summoner)
    riot_api.data_process()

    return render_template("dataDisplay.html")


@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("aboutus.html")


@app.route("/support", methods=["POST", "GET"])
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)
