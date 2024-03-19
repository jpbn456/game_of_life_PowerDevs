#!/bin/bash


#this script run "gif_geneator.py" program for all examples

for example in examples/*.json; do
    filename=$(basename -- "$example")
    base="${filename%.*}"
    echo "Processing $example..."
    python3 gif_generator.py "$example" "Outputs/${base}.csv"
done

echo "All examples processed."

