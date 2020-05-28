import json
import os

path = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(path, 'example_schema.json')
with open(file, 'r') as f:
    schema = json.load(f)
