# Open file with open function as readlines

with open("example.csv", "r") as file:
  content = file.readlines()


header = content[0:1]
rows = content[1:]

print("================HEADER===========")
print(header)
print("================ROWS===========")
print(rows)

