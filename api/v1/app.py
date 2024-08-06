#!/usr/bin/python3
"""Doced"""
import os
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """Doced"""
    storage.close()

if __name__ == "__main__":
    """Doced"""
    host = "0.0.0.0"
    port = "5000"

    if os.getenv("HBNB_API_HOST") is not None:
        host = os.getenv("HBNB_API_HOST")
    if os.getenv("HBNB_API_PORT") is not None:
        port = os.getenv("HBNB_API_PORT")
        
    app.run(debug=True, threaded=True, host=host, port=port)