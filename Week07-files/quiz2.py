# quiz2.py
# continuing quiz1.py
# The with statement will automatically close the file
# when it is finished with it

with open ("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns the number of chars written 
    print(data)
    # seven is the answer (characters in "test d\")

with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line\n")
    print (data)
    # thirteen is the answer (characters in "another line\")
    # mode "a" writes will append to an existing file


# In fact, according to the results on the lab,
# this program should print ""test d" and "another line" but mine keeps
# printing the characters numbers (7 and 13). Why?