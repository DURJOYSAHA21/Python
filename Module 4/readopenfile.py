
file1 = open("file.txt","r")
print(file1.name)
print(file1.mode)
file1.close()

with open("file.txt","r") as file2: 
    char1 = file2.read(4)
    content = file2.read()
    char2 = file2.read(4)
    
print(char1, content, char2 , char1)

with open("file.txt","r") as file2: 
    line1 = file2.readline()
    
print(line1)

with open("file.txt","r") as file2: 
    lines = file2.readlines() #readlines() reads each line as a string and keeps the newline character \n at the end.
    
print(lines[0])
print(lines[1])

with open("file.txt","r") as file2: 
    for line in file2:
        print(line, end="   ")
    
