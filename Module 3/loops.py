print(list(range(3)))
print(range(3))
print(list(range(10,15)))

squares = ["red", "yellow", "green", "blue", "orange"]
for i in range(len(squares)):
    squares[i]="white"
    
print(squares)

for square in squares:
    print(square)
    
for i,square in enumerate(squares): #enumerate print index and values in clean way
    print("index", i, "color", square)
    
fruits = ["orange", "orange", "purple", "orange"]
new_fruits = []
i=0
while i< len(fruits) and fruits[i]=="orange":
    new_fruits.append(fruits[i])
    i=i+1 
         
print(new_fruits)

for num in range(1,10):
    if num==5:
        print("breaking num: ", num)
        break
    
for num in range(1,10):
    if num==5:
        
        continue
    print(num)
    
count =0
while count<10:
    count+=1
    if count ==3:
        continue
    if count==5:
        break
    print(count)
    
    
