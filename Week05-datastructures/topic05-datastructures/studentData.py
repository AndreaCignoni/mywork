# studentData.py
# This program store a student name, her courses and grades
# Author: Andrea Cignoni

student = {
    "name":"Mary",
    "modules":[
    {
        "courseName":"Programming",
        "grade":45
    },
    {
        "courseName":"History",
        "grade":99
    }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student ["modules"]:
    print ("\t {} \t: {}".format(module["courseName"], module["grade"]))