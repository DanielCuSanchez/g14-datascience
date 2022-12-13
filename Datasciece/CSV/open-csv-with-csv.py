import csv

rows = [] # []

with open("example.csv", "r") as file:
  reader = csv.reader(file)
  print(reader)

  for rowX in reader:
    rows.append(rowX) # ["Last_name,"First name",SSN,Test1,Test2,Test3,Test4,Final,Grade", rowX, rowX]

print(rows)
header = rows[0]
content = rows[1:]

print("'----------------header--------------")
print(header)
print("'----------------content--------------")
print(content)
