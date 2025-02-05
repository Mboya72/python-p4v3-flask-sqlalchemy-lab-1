#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


# View to get an earthquake by its ID
@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.filter_by(id=id).first()  # Query for the earthquake by id
    if earthquake:
        # If the earthquake is found, return its details as JSON
        return jsonify({
            'id': earthquake.id,
            'location': earthquake.location,
            'magnitude': earthquake.magnitude,
            'year': earthquake.year
        }), 200
    else:
        # If no earthquake is found with the given id, return a 404 error with a message
        return jsonify({'message': f'Earthquake {id} not found.'}), 404


# View to get earthquakes with a magnitude greater than or equal to the given value
@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()  # Query earthquakes with a magnitude >= the given value
    
    earthquake_list = []
    for earthquake in earthquakes:
        earthquake_list.append({
            'id': earthquake.id,
            'location': earthquake.location,
            'magnitude': earthquake.magnitude,
            'year': earthquake.year
        })
    
    # Return the number of matching earthquakes and the list of their details
    return jsonify({
        'count': len(earthquake_list),
        'quakes': earthquake_list
    }), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
