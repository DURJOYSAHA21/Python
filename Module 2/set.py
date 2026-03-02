my ={1,2,3,4,6,6}
print (my)
s ={"hekko", 3.5 , "apple"}
print(s)

lis= [1,2,3,1,3,2,5]
se = set(lis)
print(se)

se2= {"mango", "apple"}
se2.add("banana")
print(se2)
se2.add("mango")
print(se2)

se2.remove("apple")
print(se2)

print("mango" in se2)
print('who' in se2)

set_1 = {"AC/DC", "Back in Black", "Rock"}
set_2 = {"AC/DC", "Back in Black", "JAzz"}
set_3 = set_1 & set_2 # also can use set1.intersection(set2)
print (set_3)

set_4 = {"AC/DC", "Back in Black", "Rock"}
set_5 = {"AC/DC", "Back in Black", "JAzz"}
set_5 = set_4 & set_5
print (set_5)

set_6 = {"AC/DC", "Back in Black", "Rock"}
set_7 = {"AC/DC", "Back in Black", "JAzz"}
set_8 = set_6 | set_7 # also can use set1.union(set2)
print (set_8)

set_9 = {"AC/DC", "Back in Black", "Rock"}
set_10 = {"AC/DC", "Back in Black"}
print (set_10.issubset(set_9))




