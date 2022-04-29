from flask import Flask, redirect, url_for, render_template, request
import riot_api
import globals
from flask_sqlalchemy import SQLAlchemy
import json
import requests

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
    item0 = db.Column(db.BIGINT)
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
        db.drop_all()
        return redirect(url_for("datadisplay", summoner=summoner))
    else:
        return render_template("summonersearch.html")


@app.route("/display/<summoner>", methods=["POST", "GET"])
def datadisplay(summoner, match_1=None, match_2=None, match_3=None, match_4=None, match_5=None,
                count=None, match_count=None):
    db.create_all()
    riot_api.data_fetch(summoner)
    summonerSpellsURL = requests.get(
        "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/summoner-spells.json")
    summonerSpellsData = summonerSpellsURL.text
    jsonSummDictionary = json.loads(summonerSpellsData)
    itemsURL = requests.get("https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1"
                            "/items.json")
    itemsData = itemsURL.text
    jsonItemDictionary = json.loads(itemsData)

    match_1 = Matches.query.filter(Matches.level_0 == 0).all()
    for z in match_1:
        if z.summonerName == summoner:
            summ1 = z.summoner1Id
            summ2 = z.summoner2Id
            item0 = z.item0
            item1 = z.item1
            item2 = z.item2
            item3 = z.item3
            item4 = z.item4
            item5 = z.item5
            item6 = z.item6
            for v in jsonSummDictionary:
                if v['id'] == summ1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner1Id = temp
                elif v['id'] == summ2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner2Id = temp
                else:
                    None
            for v in jsonItemDictionary:
                if v['id'] == item0:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item0 = temp
                elif v['id'] == item1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item1 = temp
                elif v['id'] == item2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item2 = temp
                elif v['id'] == item3:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item3 = temp
                elif v['id'] == item4:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item4 = temp
                elif v['id'] == item5:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item5 = temp
                elif v['id'] == item6:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item6 = temp

        else:
            pass
    match_2 = Matches.query.filter(Matches.level_0 == 1).all()
    for z in match_2:
        if z.summonerName == summoner:
            summ1 = z.summoner1Id
            summ2 = z.summoner2Id
            item0 = z.item0
            item1 = z.item1
            item2 = z.item2
            item3 = z.item3
            item4 = z.item4
            item5 = z.item5
            item6 = z.item6
            for v in jsonSummDictionary:
                if v['id'] == summ1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner1Id = temp
                elif v['id'] == summ2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner2Id = temp
                else:
                    None
            for v in jsonItemDictionary:
                if v['id'] == item0:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item0 = temp
                elif v['id'] == item1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item1 = temp
                elif v['id'] == item2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item2 = temp
                elif v['id'] == item3:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item3 = temp
                elif v['id'] == item4:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item4 = temp
                elif v['id'] == item5:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item5 = temp
                elif v['id'] == item6:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item6 = temp
        else:
            pass

    match_3 = Matches.query.filter(Matches.level_0 == 2).all()
    print(match_3[2].championName)
    for z in match_3:

        if z.summonerName == summoner:
            summ1 = z.summoner1Id
            summ2 = z.summoner2Id
            item0 = z.item0
            item1 = z.item1
            item2 = z.item2
            item3 = z.item3
            item4 = z.item4
            item5 = z.item5
            item6 = z.item6
            for v in jsonSummDictionary:
                if v['id'] == summ1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner1Id = temp
                elif v['id'] == summ2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner2Id = temp
                else:
                    None
            for v in jsonItemDictionary:
                if v['id'] == item0:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item0 = temp
                elif v['id'] == item1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item1 = temp
                elif v['id'] == item2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item2 = temp
                elif v['id'] == item3:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item3 = temp
                elif v['id'] == item4:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item4 = temp
                elif v['id'] == item5:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item5 = temp
                elif v['id'] == item6:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item6 = temp
        else:
            pass
    match_4 = Matches.query.filter(Matches.level_0 == 3).all()
    for z in match_4:
        if z.summonerName == summoner:
            summ1 = z.summoner1Id
            summ2 = z.summoner2Id
            item0 = z.item0
            item1 = z.item1
            item2 = z.item2
            item3 = z.item3
            item4 = z.item4
            item5 = z.item5
            item6 = z.item6
            for v in jsonSummDictionary:
                if v['id'] == summ1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner1Id = temp
                elif v['id'] == summ2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner2Id = temp
                else:
                    None
            for v in jsonItemDictionary:
                if v['id'] == item0:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item0 = temp
                elif v['id'] == item1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item1 = temp
                elif v['id'] == item2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item2 = temp
                elif v['id'] == item3:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item3 = temp
                elif v['id'] == item4:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item4 = temp
                elif v['id'] == item5:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item5 = temp
                elif v['id'] == item6:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item6 = temp
        else:
            pass
    match_5 = Matches.query.filter(Matches.level_0 == 4).all()
    for z in match_5:
        if z.summonerName == summoner:
            summ1 = z.summoner1Id
            summ2 = z.summoner2Id
            item0 = z.item0
            item1 = z.item1
            item2 = z.item2
            item3 = z.item3
            item4 = z.item4
            item5 = z.item5
            item6 = z.item6
            for v in jsonSummDictionary:
                if v['id'] == summ1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner1Id = temp
                elif v['id'] == summ2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/DATA/Spells/Icons2D', '')
                    temp = temp.lower()
                    z.summoner2Id = temp
                else:
                    None
            for v in jsonItemDictionary:
                if v['id'] == item0:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item0 = temp
                elif v['id'] == item1:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item1 = temp
                elif v['id'] == item2:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item2 = temp
                elif v['id'] == item3:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item3 = temp
                elif v['id'] == item4:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item4 = temp
                elif v['id'] == item5:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item5 = temp
                elif v['id'] == item6:
                    temp = v['iconPath']
                    temp = temp.replace('/lol-game-data/assets/ASSETS/Items/Icons2D', '')
                    temp = temp.lower()
                    z.item6 = temp

        else:
            pass
    match_list = []
    match_list.append(match_1)
    match_list.append(match_2)
    match_list.append(match_3)
    match_list.append(match_4)
    match_list.append(match_5)
    count = Matches.query.count()
    count = int(count / 10)

    return render_template("dataDisplay.html", summoner=summoner, match_1=match_1, match_2=match_2, match_3=match_3,
                           match_4=match_4, match_5=match_5, count=count, match_list=match_list,
                           match_count=match_count)


@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("aboutus.html")


@app.route("/support", methods=["POST", "GET"])
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)
