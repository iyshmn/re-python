# file1 = open("test.txt")#read mode
# print(file1.read())
# file1.close()
# file2 = open("new.txt",'w')
#     # TODO: write code...
try:
    file1=open("test.txt")
    print(file1.read())
finally:
    file1.close()
    
with open("test.txt") as file2:
    print(file2.read())