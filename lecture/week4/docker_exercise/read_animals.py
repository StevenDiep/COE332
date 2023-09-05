#!/usr/bin/env python3

import sys
import json
import random

with open(sys.argv[1], 'r') as f:
    data = json.load(f)

animals = data['animals']
print(random.choice(animals))
