# the with statement will automatically close the file
# when it is finished with it
FILENAME = "test-a.txt"

with open ("test-a.txt") as f:
    data = f.read() 
    print(data)

# Answer is FileNotFoundError [Errno 2] No such file or directory
# the old way of doing this is
# f = open("test1.txt")
# data = f.read()
# print(data)
# f.close()