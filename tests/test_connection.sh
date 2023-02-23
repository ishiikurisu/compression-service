#!/bin/sh
set -ex

# decompress file
curl -X POST \
     -F 'filename=compressed_file.tar.gz' \
     -F 'upload=@compressed_file.tar.gz' \
     http://localhost:5000/extract

# TODO compress file

