#!/bin/sh
set -ex

# decompress file
curl -X POST \
     -F 'filename=compressed_file.tar.gz' \
     -F 'upload=@compressed_file.tar.gz' \
     http://localhost:5000/extract

# compress file
curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"url.txt": "http://www.crisjr.eng.br\n", "notes.md": "# Notes\n\nNothing yet really...\n"}' \
     --output 'compressed_contents.tar.gz' \
     http://localhost:5000/compress

tar -xvf compressed_contents.tar.gz
cat url.txt
cat notes.md
rm url.txt
rm notes.md 
rm compressed_contents.tar.gz

