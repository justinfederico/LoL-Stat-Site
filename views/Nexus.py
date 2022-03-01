from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("test.html", summonerName="Fed")

@app.route("/admin")
def admin():
    return redirect(url_for("/"))

if __name__ == "__main__":
    app.run(debug=True)
