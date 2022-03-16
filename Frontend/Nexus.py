from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#Defining routes for the site, directing the user to the desired page
@app.route("/logoclick", methods=["POST", "GET"])
def logoclick():
    return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/champions", methods=["POST", "GET"])
def champions():
    return render_template("champions.html")

@app.route("/lookup", methods=["POST", "GET"])
def lookup():
    return render_template("summonersearch.html")

@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("aboutus.html")

@app.route("/support", methods=["POST", "GET"])
def support():
    return render_template("support.html")

if __name__ == "__main__":
    app.run(debug=True)
