#!/usr/bin/python3
'''
    app to register blueprint and start up flask
'''
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def closeStorageAfterRequest(error):
    """
    Teardown method to close the storage
    """
    storage.close()
    storage.reload()


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles errors and returns a JSON-formatted 404 status code response
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(
        host=getenv('HBNB_API_HOST', '0.0.0.0'),
        port=getenv('HBNB_API_PORT', 5000),
        threaded=True
    )
