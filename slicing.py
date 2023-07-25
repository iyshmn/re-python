name = "ayushman prakash"
for letters in range(len(name)):
    print(name[letters]+" "+str(letters))
first_name = name[slice(8)]
print(first_name)
second_name = name[slice(9,16)]
print(second_name)