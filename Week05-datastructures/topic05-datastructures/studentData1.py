# studentData1.py
# labWeek5 question 4
# This program keep reading in students' modules and grades
# until the user enters a blank module name

student2 = {
    "Name":" ",
    "modules": [
    {
        "courseName":" History ",
        "grade": "68"
    },
    {
        "courseName":"Maths ",
        "grade":"53 "
    }
    ]
}
student2 = input("Enter a name: ")
print ("Student: ", student2 ).format(student["name"])
for module in student ["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))