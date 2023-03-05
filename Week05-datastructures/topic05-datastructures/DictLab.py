# DictLab
# Week5 quiz lab
# Author: Andrea Cignoni

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ("Jan", "Feb", "Mar")
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict (firstname = "joe")
me = {
    "firstName" : "Andrew",
    "teaching" : [{
    "courseName" : "programming",
    "semester" : 1
    }, {
    "courseName" : "Data Representation",
    "semester" : 2
    }
    ]
}
print("Value of key NumberOfQuestions is a ", type(5))
print("Value of key AverageAge is a ", type(23.4))
print("Value of key debugMode is a ", type(True))
print("Value of key name is a ", type("joe"))
print("Value of key ages is a ", type([]))
print("Values of key months are ", type('Jan'), type('Feb'), type('Mar'))
print("Value of key months[1] is a ", type('Jan'))
print("Value of key book is a ", type({}))
print("Value of key stuff is a ", type([ 12,'Fred', False, {}]))
print("Value of key stuff[2] is a ", type('Fred'))
print("Value of key someone is a ", type(dict(firstname = "joe")))
print("Value of key someone ['firstname'] is a ", type("joe"))
print("Value of key me is a ", type({}))
print("Value of key me ['teaching'] is a ", type([]))
print("Values of key me ['teaching'] [0] ['semester'] are ", type(['teaching']),type([0]),type(['semester']))
print("Values of key ['teaching'] [0] ['coursename] are ", type(['teaching']),type([0]), type(['coursename']))