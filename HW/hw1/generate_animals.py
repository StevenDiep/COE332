import json
import random
import argparse
import petname


#Pre set data needed to generate the animal
data = {}
data['animals'] = []
random.seed(1)
head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']

#Code that is needed to generate the body of our animal
parser = argparse.ArgumentParser(description="Generate human readable random names")
parser.add_argument("-w", "--words", help="Number of words in name, default=2", default=2)
parser.add_argument("-s", "--separator", help="Separator between words, default='-'", default="-")
parser.options = parser.parse_args()

#Looping through and creating the 20 animals
for i in range(20):
    animal = {}
    animal['head'] = random.choice(head_list)
    animal['body'] = petname.Generate(int(parser.options.words), parser.options.separator)
    animal['arms'] = random.randint(2,10)
    animal['legs'] = random.randint(3,12)
    animal['tail'] = animal['arms'] + animal['legs']
    
    data['animals'].append(animal)

#Dumping data into a json file
with open('animals.json', 'w') as out:
    json.dump(data, out, indent=2)