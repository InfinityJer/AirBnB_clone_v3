#!/usr/bin/python3
'''
    flask with general route /status
    Contains index view for the API
'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Return a JSON response with status OK
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """
    Retrieves the number of each objects by type
    """
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    counts = {key: storage.count(val) for key, val in classes.items()}
    return jsonify(counts)
