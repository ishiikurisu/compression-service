from io import BytesIO

from flask import (
    Flask,
    # request,
    # send_file,
)
from flask_cors import CORS

import compression as tar

app = Flask(__name__)
CORS(app)


@app.route("/extract", methods=["POST"])
def extract():
    # TODO complete me!
    return "not implemented yet!"


@app.route("/compress", methods=["POST"])
def compress():
    # TODO complete me!
    return "not implemented yet!"

