import numpy as np

a = np.arange(15).reshape(3, 5)
a2 = np.arange(50)

print(a)
print(a.size)
print(a.shape)
print(a.ndim)
print(type(a))
print(a2)
print(a2.size)
print(a2.shape)
print(a2.ndim)

a3 = np.array(["melon", "sandia", "cereza", " manzana"])

print(a3)


a4 = np.array([[[1,2,3]],[[4,5,6]],[[7,8,9]]])
print(a4.size)
print(a4.shape)
print(a4.ndim)
print(a4[2][0][1])

for x in a4:
  for y in x:
    for z in y:
      print(z)


for x in a4:
  print(x)

for x in np.nditer(a4[0:2]):
  print(x)