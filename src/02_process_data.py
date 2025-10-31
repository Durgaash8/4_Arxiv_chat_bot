import os
import json
import csv

# ------------------------------
# Paths (auto-detect relative to script)
# ------------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_dir, "../data/quantum_subset.json")
output_path = os.path.join(base_dir, "../data/quantum_subset.csv")

# ------------------------------
# Read JSON file
# ------------------------------
try:
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("JSON file loaded successfully!")
except FileNotFoundError:
    print(f"Error: JSON file not found at {input_path}")
    exit(1)

# ------------------------------
# Convert to CSV
# ------------------------------
# Assuming JSON is a list of dictionaries
if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
    keys = data[0].keys()
    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        dict_writer = csv.DictWriter(csv_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"CSV file saved successfully at {output_path}")
else:
    print("Error: JSON format is not a list of dictionaries.")
