from flask import flask

app = Flask(__main__)

@app.route("/")
def home():
  return "This is the main page. <h1>MAIN PAGE<h1>"


if __name__ == "__main__":
  app.run()
