import argparse

dict_example = {}

dict_example['head'] = {'raven':0}
dict_example['head']['raven'] += 1

print(type(dict_example) == dict )