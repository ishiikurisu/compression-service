from io import BytesIO
import json

from flask import (
    Flask,
    request,
    send_file,
)
from flask_cors import CORS

import compression as tar

app = Flask(__name__)
CORS(app)


@app.route("/extract", methods=["POST"])
def extract():
    contents = None
    for _, file_storage in request.files.items():
        contents = file_storage.read()
        break

    decompressed_contents = tar.extract(contents)
    if decompressed_contents is None:
        return '{"error": "Failed to decompress file"}'

    return json.dumps(decompressed_contents)


@app.route("/compress", methods=["POST"])
def compress():
    # TODO complete me!
    return "not implemented yet!"

