"""Render views on navigator"""
import app.maps as maps
import app.parser as parser
import app.wiki as wiki
from flask import jsonify, render_template, request

from . import GMAPS
from .main import APP  # pylint: disable=cyclic-import


@APP.route("/")
def home():
    """
    Main page render

    :return: _render
    """
    return render_template("index.html", gmaps=GMAPS)


@APP.route("/question", methods=["POST"])
def question():
    """
    /question page process

    :return: Dict
    """
    questions = request.data.decode("utf-8")

    parsed = parser.prepare(questions)

    locations = maps.get_location(parsed)

    address = [location["address"] for location in locations if location]

    coordonates = [location["coordonates"] for location in locations if location]

    ret = wiki.endow(wiki.get_info_on_loc(coordonates, parsed))

    return jsonify(message=ret, coordonates=coordonates, address=address)
