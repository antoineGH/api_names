from flask import Blueprint, jsonify, render_template, request
from . import Person

name = Blueprint('name', __name__)

@name.route('/')
def home():
    return render_template('documentation.html', title='Documentation')

@name.route('/api/gender', methods=['POST'])
def get_gender():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    content = request.get_json(force=True)    
    name = content.get("name", None)
    if not name: 
        return jsonify({"error": 'Missing name in JSON'})
    person = Person(name)
    gender = person.get_gender()
    return jsonify(gender)

@name.route('/api/nation', methods=['POST'])
def get_nation():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    content = request.get_json(force=True)    
    name = content.get("name", None)
    if not name: 
        return jsonify({"error": 'Missing name in JSON'})
    person = Person(name)
    nation = person.get_nationality()
    return jsonify(nation)

@name.route('/api/age', methods=['POST'])
def get_age():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    content = request.get_json(force=True)    
    name = content.get("name", None)
    if not name: 
        return jsonify({"error": 'Missing name in JSON'})
    person = Person(name)
    age = person.get_age()
    return jsonify(age)