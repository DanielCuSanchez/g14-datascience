# Dictionaries: They are similar like objects in JS, the way the data is stored is with keys and values.

student = {
  "name": "Emilio",
  "state": "Puebla",
  "age": "27"
}

print(type(student))
print(student)

# Looping dictionary

for key in student.keys(): # ["Name", "state", "age"]
  print(key)

for value in student.values(): # ["Emilio", "Puebla", "27"]
  print(value)

for key, value in student.items(): # [["name": "Emilio"],["state": "Puebla"],[ "age": "27"]]
  print(f"KEY = {key}, VALUE = {value}")