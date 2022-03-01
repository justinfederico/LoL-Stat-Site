from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#Defining routes for the site, directing the user to the desired page
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return redirect(url_for("/"))

if __name__ == "__main__":
    app.run(debug=True)
