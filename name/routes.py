from flask import request, Blueprint, jsonify, render_template

name = Blueprint('name', __name__)

@name.route('/')
def home():
    return render_template('documentation.html', title='Documentation')