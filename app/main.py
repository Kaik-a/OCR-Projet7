"""Flask launch"""
from flask import Flask

from . import views  # pylint: disable=unused-import, wrong-import-position

APP: Flask = Flask(__name__)
