from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  #return "Hello World"
  return render_template("home.html")
  return render_template("LSTM Model.py")

if __name__ == "__main__":
  app.run(host= "0.0.0.0", debug=True)