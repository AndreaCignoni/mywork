# Json Test
# Json is a standard way of storing objects
# mainly used to create files with Dict or lists

import json
FILENAME="testdict.json"
""""
sample= dict(name='fred', age=31, grades=[1,34,55])

def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)
# a file named {} testdict.json was created with the above dictionary
writeDict(sample)
"""
def readDict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty dict
    # this can be done later
    with open (FILENAME) as f:
        return json.load(f)
    
somedict = readDict()
print (somedict)