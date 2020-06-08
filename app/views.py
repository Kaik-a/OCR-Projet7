from flask import jsonify, render_template, request

from . import app
import app.wiki as wiki
import app.maps as maps
import app.parser as parser

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question", methods=["POST"])
def question():
    questions = request.form['name_input_question']
    coordonates = maps.get_location(parser.prepare(questions))
    ret = wiki.endow(wiki.get_info_on_loc(coordonates))
    return jsonify(ret)
