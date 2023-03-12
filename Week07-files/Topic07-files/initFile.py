# initFile.py
# This program initializes the file and writes inputs given

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print ("File does not exist")
    # initialise file here

def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previous runs
        return 0