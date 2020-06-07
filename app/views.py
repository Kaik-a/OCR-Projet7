from flask import jsonify, render_template, request

from . import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question", methods=["POST"])
def question():
    question = request.form["id_form"]
    return jsonify(["no answer"])
