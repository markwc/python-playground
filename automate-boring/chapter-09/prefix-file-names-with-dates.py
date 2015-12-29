#!/usr/bin/python

import datetime
import os
import shutil
import sys

def modificationDate(fileName):
    timeStamp = os.path.getctime(fileName)
    return datetime.datetime.fromtimestamp(timeStamp).strftime('%y%m%d%H%M%S')

if __name__ == "__main__":
    for oldFileName in sys.argv[1:]:
        fileDate = modificationDate(oldFileName)
        newFileName = fileDate + '-' + oldFileName
        print (oldFileName + ' --> ' + newFileName)
        shutil.move(oldFileName, newFileName)
