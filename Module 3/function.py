def add(a):
    b=a+1;
    print(a,"if you add one",b)
    return b

def mult(a,b):
    c=a*b
    return c
    print("multi")
    
def MJ():
    print("The MJ")
    
def MJ1():
    print("the mj1")
    return None
 
def con(a,b):
    return a+b   
    
def typesong(song,year):
    print(song,year)
    if year>1980:
        return "Modern"
    else:
        return "Oldie"
    
def lis(lis):
    for element in lis:
        print(element)
        
def check(tex):
    if tex in string:
        return "MAtch"
    else:
        return "not match"
    
def checks(x,y):
    if x==y:
        return 1

def fre(string):
    words =[]
    words =string.split()
    dic ={}
    for key in words:
        dic[key]=words.count(key)
    print("the freq of words ",dic)
    
def isgood(rait=4):
    if(rait<7):
        
        print(rait)
        
    else:
        print(rait)
        

string = "Durjoy"
add(1)
help(add)
add(2)

result = mult(12,2)
print(result)
result = mult(10.0,3.14)
print(result)
print(mult(2,"Durjoy")) 
print(MJ()) #The function runs first. Then whatever the function returns gets printed.
print(MJ1())

print(con("this","is"))

a=(1,2,3)
c=sum(a)
print(f"The sum of tuple {c}")

x=typesong("sonic", 1982)
print(x);

lis(['1',1,"the ","abe"])
print(check("Durjoy"))

string1="SAHA"
string2="SAHA"
if(checks(string1,string2))==1:
    print("both match")
else:
    print("no")

fre("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

isgood()
isgood(10)

album = "The BodyGuard"
def printer1(album):
    global interval_var1
    interval_var1= "Thriller"
    print(album, "is an album")
    
printer1(album )
printer1(interval_var1)

myfav="DURJOY"
def getrait(band):
    myfav="SAHA"
    if band==myfav:
        return 10;
    else:
        return 0;
    
print(getrait("Onno"))
print(getrait("DURJOY"))
print(getrait("SAHA"))
print(myfav)

def printall(*args):
    print(len(args))
    for e in args:
        print(e)
        
printall('Horsefeather','Adonis','Bone')
printall('Horsefeather','Adonis','Bone',"seo")

def printdic(**args):
    for key in args:
        print(key, ":", args[key])
        
printdic(Country='Canada',Province='Ontario',City='Toronto')

def additem(list):
    list.append("another")
    
li =["one"]
print(additem(li))
print(li)

print(con(['a',1],["b",1]))
print(con((1, 2), (3, 4)))