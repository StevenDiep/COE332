#!/usr/bin/env python3

import json
import random
import petname
import redis

rd = redis.StrictRedis(host='127.0.0.1', port=5040, db=0)

#Pre set data needed to generate the animal
data = {}
data['animals'] = []
random.seed(1)
head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']

#Looping through and creating the 5 animals
for i in range(5):
    animal = {}
    animal['head'] = random.choice(head_list)
    animal['body'] = petname.name() + '-' + petname.name()
    animal['arms'] = random.randint(1,5) * 2
    animal['legs'] = random.randint(1,4) * 3
    animal['tail'] = animal['arms'] + animal['legs']
    
    rd.hset('r'+ str(i), mapping=animal)


