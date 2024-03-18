#!/bin/bash

# Navigate to the script directory if necessary
# cd /path/to/your/script

for example in examples/*.json; do
    filename=$(basename -- "$example")
    base="${filename%.*}"
    echo "Processing $example..."
    python3 gif_generator.py "$example" "Outputs/${base}.csv"
done

echo "All examples processed."

