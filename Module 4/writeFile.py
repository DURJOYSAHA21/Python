with open ("write.txt","w") as file1:
    file1.write("This is a new line\n")
    file1.write("This is a new another line\n")
    
lines=["Line from list\n","Line from list new\n"]
with open("write.txt","w") as file1:
    for line in lines:
        file1.write(line)

        
with open("file.txt","r") as readfile:
    with open("write.txt","w") as writefile:
        for lines in readfile:
            writefile.write(lines)
            

lines=["Line from list\n","Line from list new\n"]         
with open("write.txt","a") as file1:
    for line in lines:
        file1.write(line)
        
        
        