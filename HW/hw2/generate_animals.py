#!/usr/bin/env python3

import json
import random
import argparse
import petname
import sys

#Pre set data needed to generate the animal
data = {}
data['animals'] = []
random.seed(1)
head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']

#Looping through and creating the 20 animals
for i in range(20):
    animal = {}
    animal['head'] = random.choice(head_list)
    animal['body'] = petname.name() + '-' + petname.name()
    animal['arms'] = random.randint(1,5) * 2
    animal['legs'] = random.randint(1,4) * 3
    animal['tail'] = animal['arms'] + animal['legs']
    
    data['animals'].append(animal)

#Dumping data into a json file
with open(sys.argv[1], 'w') as out:
    json.dump(data, out, indent=2)
