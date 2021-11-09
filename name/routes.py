from flask import Blueprint, json, jsonify, render_template
from . import Genderize

name = Blueprint('name', __name__)

@name.route('/')
def home():
    return render_template('documentation.html', title='Documentation')

@name.route('/api/name')
def get_name():
    gender = Genderize()
    gender.say_hello()
    return jsonify({"message": "OK"}), 200