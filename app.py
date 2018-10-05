from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/tour")
def tour():
    return render_template("tour.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

