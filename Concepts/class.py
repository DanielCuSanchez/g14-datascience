class Car:
  model = ""
  year = ""
  brand = ""

  def __init__(self, model, year, brand):
    self.model = model
    self.year = year
    self.brand = brand
# Forma 1
  def __str__(self):
    # example = self.model + "+" + self.year
    return f"{self.model} + {self.year} + {self.brand}" # `${Variable} texto ${variable} `


tesla = Car("S", 2022, "Tesla")

# Forma 2
print(tesla.model,tesla.year,tesla.brand, sep="-")
print(tesla.year,tesla.brand,end =' - ')
print(tesla.model)

print("Example: ", tesla)
print(type(tesla))


# number1 = int(3)
# print(number1)
