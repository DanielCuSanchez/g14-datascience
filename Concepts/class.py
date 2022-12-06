class Car:
  model = ""
  year = ""
  brand = ""

  def __init__(self, model, year, brand):
    self.model = model
    self.year = year
    self.brand = brand


tesla = Car("S", 2022, "Tesla")

print(tesla)
print(type(tesla))


# number1 = int(3)
# print(number1)
