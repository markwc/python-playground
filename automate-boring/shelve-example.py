#!/usr/bin/python3

import os
import shelve

my_file = 'mydata'

# Put a cats list on the shelf.
shelf_file = shelve.open(my_file)
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()

# Copy the cats list from the shelf.
cats = []
print('cats before = ', cats)
shelf_file = shelve.open(my_file)
print('mydata is of type ', type(shelf_file))
cats = shelf_file['cats']
print('cats after = ', cats)
shelf_file.close()

# Read the shelf dictionary.
shelf_file = shelve.open(my_file)
print('mydata keys = ', list(shelf_file.keys()))
print('mydata values = ', list(shelf_file.values()))
shelf_file.close()

# Clean up!
os.remove(my_file)
