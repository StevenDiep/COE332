import json
import random

with open('animals.json', 'r') as f:
    data = json.load(f)

animals = data['animals']
print(random.choice(animals))
