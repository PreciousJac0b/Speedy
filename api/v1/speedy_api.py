#!/usr/bin/env python3
"""api module"""

from flask import Flask, jsonify
from flask_cors import (CORS, cross_origin)
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {'origins': "*"}})

@app.route('/status',methods={'GET'})
def status():
    return jsonify({'status': 'OK'})

if __name__ =="__main__":
    app.run(host='0.0.0.0', port='5050')