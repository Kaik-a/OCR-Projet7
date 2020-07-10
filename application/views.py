import application.maps as maps
import application.parser as parser
import application.wiki as wiki
from flask import jsonify, render_template, request

from . import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question", methods=["POST"])
def question():
    questions = request.data.decode("utf-8")
    parsed = parser.prepare(questions)
    locations = maps.get_location(parsed)
    address = [location["address"] for location in locations if location]
    coordonates = [location["coordonates"] for location in locations if location]
    ret = wiki.endow(wiki.get_info_on_loc(coordonates, parsed))
    return jsonify(message=ret, coordonates=coordonates, address=address)
