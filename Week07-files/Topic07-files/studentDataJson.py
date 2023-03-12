# Student Data Jason
# Menu Item called Save in student management program
# Author: Andrea Cignoni

students= []

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q)").strip()
    return choice

def doAdd(students):
    # code here to add
    print("in adding")

def doView (students):
    # code here to view
    print("in adding")

def doSave(students):
    # call to save dict
    print("in save")
    
# main program
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