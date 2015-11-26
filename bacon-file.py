#!/usr/bin/python3
my_file = 'bacon.txt'
bacon_file = open(my_file, 'w')
stuff_to_write = 'Hello world!'
n = bacon_file.write(stuff_to_write + '\n') - 1
print ('wrote "' + stuff_to_write + '", which is ', n, ' characters')
bacon_file.close()
bacon_file = open(my_file, 'a')
bacon_file.write('Bacon is not a vegetable')
bacon_file.close()
bacon_file = open(my_file)
content = bacon_file.read()
bacon_file.close()
print(content)

import os
os.remove(my_file)
