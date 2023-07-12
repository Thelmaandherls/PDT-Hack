from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
  return render_template("home.html")
  
@app.route("/welldone/")
def welldone():
    return render_template("welldone.html")

@app.route("/stockprediction/")
def stockprediction():
    return render_template("stockprediction.html")

@app.route("/tradingbot/")
def tradingbot():
    return render_template("tradingbot.html")

if __name__ == "__main__":
  app.run(host= "0.0.0.0", debug=True)
