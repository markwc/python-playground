#!/usr/bin/python3

import shutil
import os

cwd = os.getcwd()
spamFile = os.path.join(cwd , 'spam.txt')
spam = open(spamFile, 'a')
spam.close()
print(spamFile)
spamDirectory = os.path.join(cwd, 'delicious')
os.makedirs(spamDirectory)
print('copying ' + spamFile + ' to ' + spamDirectory)
shutil.copy(spamFile, spamDirectory)
shutil.rmtree(spamDirectory)
os.unlink(spamFile)
