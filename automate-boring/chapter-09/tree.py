#!/usr/bin/python

import os

cwd = os.getcwd()
for folderName, subfolders, filenames in os.walk(cwd):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('|--- /' + subfolder)
    for filename in filenames:
        print('|--- '+ filename)
    print('')
