#!/bin/bash

#this script run "create_frames.py" for all example

for example in examples/*.json; do
    filename=$(basename -- "$example")
    base="${filename%.*}"
    echo "Processing $example..."
    python3 generatePDM.py "$example"
done

echo "All examples processed."

