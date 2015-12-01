#!/usr/bin/python3

import pprint
import os

# create a list of dictionaries
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

# import pprint and print cats
print(pprint.pformat(cats))

# Use pprint to save off a python command to a file
my_file = 'my_cats.py'
file_object = open(my_file, 'w')
file_object.write('cats = ' + pprint.pformat(cats) + '\n')
file_object.close()

# clear the cats variable
cats = []
print('cats before = ', cats)

# Now import from saved file and print the list.
import my_cats
print('cats = ', my_cats.cats)
print('cat[0] = ', my_cats.cats[0])

# clean up!
os.remove(my_file)
