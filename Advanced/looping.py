# loops in python

myList = ["Emilio","Francisco", "Bruno", "Rogelio", "Luis", "Luis"]


# Looping with for in
for x in myList:
  print(x, '😀' , x)

# Looping with for in range -> range is a function
for x in range(len(myList)):
  print(x, '😁' , myList[x])

for x in range(100):
  print(x +1, '😁' )