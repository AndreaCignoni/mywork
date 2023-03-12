# quiz1.py
# continuing quiz.py

with open ("test-b.txt", "w") as f:
    data = f.write("test b\n") # returns the number of chars written

with open("test-b.txt", "w") as f2:
    data = f2.write("another line\n")
    print (data)
    # thirteen is the answer (characters in "another line\")

# the "w" mode should create the file and delete 
# the previous if already exist
# In fact, according to the results on the lab
# this program should print "Another line" but mine keeps
# printing the characters numbers (7 and 13). Why?