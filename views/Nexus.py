from flask import Flask, redirect, url_for, render_template

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

#Defining routes for the site, directing the user to the desired page
@app.route("/")
def home():
    return render_template("homePage.html", summonerName="Fed")

@app.route("/admin")
def admin():
    return redirect(url_for("/"))

if __name__ == "__main__":
    app.run(debug=True)
