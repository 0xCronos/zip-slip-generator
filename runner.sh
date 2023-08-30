#!/bin/bash


OUTPUT='malicious.zip'

python3 main.py \
    --file payload.php \
    --depth 5 \
    --path /sample/ \
    --output $OUTPUT

if [ -e $OUTPUT ]; then
    unzip -l $OUTPUT
else
    echo "[ERROR] The output file has not been generated."
fi