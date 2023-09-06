#!/usr/bin/env python3

import json
import random
import sys

def generate_summary(data):
    stats = {};
    stats['head_count'] = {'snake':0, 'bull':0, 'lion':0, 'raven': 0, 'bunny':0}
    total_arms = 0
    total_legs = 0
    
    for animal in data:
        stats['head_count'][animal['head']] += 1
        total_arms += animal['arms']
        total_legs += animal['legs']
        
    stats['avg_arms'] = total_arms / len(data)
    stats['avg_legs'] = total_legs / len(data)
    stats['avg_tails'] = stats['avg_arms'] + stats['avg_legs']
    
    return stats


with open(sys.argv[1], 'r') as f:
    data = json.load(f)

animals = data['animals']
stats = generate_summary(animals)

print(stats)

