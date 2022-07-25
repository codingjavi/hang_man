import json

with open('states.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    print(fcc_data)