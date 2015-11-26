#!/usr/bin/python3

import shelve
shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()

cats = []
print('cats before = ', cats)
shelf_file = shelve.open('mydata')
print('mydata is of type ', type(shelf_file))
cats = shelf_file['cats']
print('cats after = ', cats)
shelf_file.close()

shelf_file = shelve.open('mydata')
print('mydata keys = ', list(shelf_file.keys()))
print('mydata values = ', list(shelf_file.values()))
shelf_file.close()
