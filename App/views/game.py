from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
   get_all_words_json,
)


game_views = Blueprint('game_views', __name__, template_folder='../templates')
