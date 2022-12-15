import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


file = pd.read_csv("file-load.csv")

dataset = file["Final"]

print(dataset)

mean =  np.mean(dataset)
median =  np.median(dataset)
var =  np.var(dataset)
std =  np.std(dataset)
percentile =  np.percentile(dataset, 45)

print("mean", mean)
print("median", median)
print("var", var)
print("std", std)
print("percentile", percentile)


arr = np.random.uniform(0.0, 0.5, 3000)
arr2 = np.random.normal(0.0, 0.5, 3000)

#plt.hist(arr2, 100)

#plt.show()

print(arr)


# Linear regression

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#Since here

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()