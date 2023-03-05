# Student Management 1
# Program Student Management will now display 
# the menu until the user picks q and if option a
# is selected the program will return a function 
# called doView()
# Author: Andrea Cignoni

students = []
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q)").strip()
    return choice

def getModules():
    modules = []
    modulesname = input ["please enter  the module name (blank to quit)"]
    while (modulesname != ""):
        module = {}
        module["name"]= modulesname
        module["grade"] = int(input("enter grade"))
        modules.append(module)

        modulesname = input("please enter the module name")

    return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]= input("please enter name: ")
    currentStudent["modules"]= readModules ()

    students.append(currentStudent)
    
def doView(students):
    for student in students:
        print (student["name"])
        for module in student:
            print("\t", module["name"], ":", module["grade"]) 
    
# main program
choice = displayMenu()
while (choice != 'q'):
    # we could do this with labda functions
    # this kept basic on purpose
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu ()
def readModules():
    return[]


#test

print(students)