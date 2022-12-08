# Lists comprehensions: They are a shorter version of a list declaration, it is used to filter, modify and remove data.

myList = ["Emilio","Francisco", "Bruno", "Rogelio", "Luis", "Luis"]




# newList = myList.map(e => e != "Luis") in JS
newList = [ element for element in myList if element != "Luis" ]

print(myList)
print(newList)