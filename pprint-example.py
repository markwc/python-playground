#!/usr/bin/python3

# create a list of dictionaries
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# import pprint and print cats
import pprint
print(pprint.pformat(cats))
# Use pprint to save off a python command to a file
file_object = open('my_cats.py', 'w')
file_object.write('cats = ' + pprint.pformat(cats) + '\n')
file_object.close()
# clear the cats variable
cats = []
print('cats before = ', cats)
# now import from saved file
import my_cats
# print the cats list
print('cats = ', my_cats.cats)
print('cat[0] = ', my_cats.cats[0])

