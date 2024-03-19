#!/bin/bash

#this script run "create_frames.py" for all example

for example in examples/*.json; do
    filename=$(basename -- "$example")
    base="${filename%.*}"
    echo "Processing $example..."
    python3 create_frames.py "$example" "Outputs/${base}.csv"
done

echo "All examples processed."

