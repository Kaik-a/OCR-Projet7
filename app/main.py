"""Flask launch"""
from flask import Flask

APP: Flask = Flask(__name__)

from . import views  # pylint: disable=unused-import, wrong-import-position
