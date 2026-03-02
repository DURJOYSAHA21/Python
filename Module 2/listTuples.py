# create tuple
raiting =(1,2,3,4)
print(raiting)
print(type(raiting))

#mixed
T =("Name", 10, 1.2)
print (T)

print(raiting[0])
print(raiting[-1])
print(raiting[-3])
print(raiting[1:])

new =raiting + T
print(new)

print (raiting[0:3])
print(raiting[-2:]) #last 2 ele

print(len(raiting))
#tuple are immutable not able to change by indexing
raiting = (5,6,7,2,9)
print(raiting)

raiting =tuple(sorted(raiting))
print(raiting)

Nt =(1, 2, ("a","b"), (10,20))
print(Nt[2])
print(Nt[2][1])


#list
l =["name", 10, 1.2]
print(l)
l[0]="new"
print(l)
l.extend([2,5]) # adds indivually
print(l)
l.append([4,5]) # adds as single element
print(l)

L = ["hard rock", 10, 1.2]
del L[0]
print(L)
s =L[0].split()
print(s)
st= "A,B,C"
stri =st.split(",")
print(stri)

B =  ["hard rock", 10, 1.2]
C =B #ref pass alias
B[0]="banana";
print(B)
print(C)

D=  ["hard rock", 10, 1.2]
E=D[:] #make clone not ref
D[0]="banana";
print(D)
print(E)

