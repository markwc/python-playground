#!/usr/bin/python3

import os

my_file = 'bacon.txt'

# Write some stuff out to a file
bacon_file = open(my_file, 'w')
stuff_to_write = 'Hello world!'
n = bacon_file.write(stuff_to_write + '\n') - 1
print ('wrote "' + stuff_to_write + '", which is ', n, ' characters')
bacon_file.close()

# Append some stuff to that file.
bacon_file = open(my_file, 'a')
bacon_file.write('Bacon is not a vegetable')
bacon_file.close()

# Read the file.
bacon_file = open(my_file)
content = bacon_file.read()
bacon_file.close()
print(content)

# Clean up!
os.remove(my_file)
