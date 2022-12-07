# Sets: They are unordered, unchangeable, unindexed and they can not accept duplicated values. It is case sensitive.

mySet = {"e1", "e2", "e3", "e3", "e3", "E3", "E3", True, 1.2, 4} #can not accept duplicated values and it is case sensitive.

#print(mySet[0]) #They are unindexed
print(mySet) #They are unordered
print(type(mySet))

mySet.add("E4")
mySet.remove("e2")
print(mySet) #They are unordered


exampleList = list(mySet)

print(type(exampleList))
print(exampleList)


#for x in mySet:
 # print(x)