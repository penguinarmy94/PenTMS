from flask import Flask, render_template, request
from typing import Dict
import functions

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template("./index.html")

@app.route("/park", methods=["POST"])
def national_park_route():
    name: str = request.form['name']
    species: str = request.form['species']
    legs: int = int(request.form['legs'])
    wildlife: functions.Wildlife  = functions.Wildlife(name=name, species=species, number_of_legs=legs)
    context: Dict[str,str] = { "wildlife" : wildlife }
    return render_template("./response.html", **context)


if __name__ == "__main__":
    app.run("0.0.0.0", port=9500)