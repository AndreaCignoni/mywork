# Student Management 1
# Program Student Management will now display 
# the menu until the user picks q and if option a
# is selected the program will return a function 
# called doView()
# Author: Andrea Cignoni

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q)").strip()
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]= input("please enter name: ")
    currentStudent["modules"]= readModules ()
    students.append(currentStudent)

def readModules():
    modules = []
    modulesname = input ("Please enter  the first Module name (blank to quit):").strip()
    
    while (modulesname != ""):
        module = {}
        module["name"]= modulesname
        module["grade"] = int(input("\t\Enter grade"))
        modules.append(module)

        modulesname = input("\tPlease enter the module name").strip()

    return modules

def displayModules (modules):
    print("\tName   \tGrade")
    for module in modules:
        print (f"\t{ module["name"]} \t{ module["grade"]}")

def doView (students):
    for currentStudent in students:
        print (currentStudent["name"])
        displayModules (currentStudent ["modules"])
    
# main program
students = []
choice = displayMenu()
while (choice != 'q'):
    # we could do this with lambda functions
    # this kept basic on purpose
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu ()