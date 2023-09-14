import json

def get_data():
    with open('animals.json', 'r') as file:
        data = json.load(file)
    
    return data

test = get_data()