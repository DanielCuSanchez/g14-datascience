
# Lambda functions: Is a reserved word for using to create shorter versions of functions.

# lambda arguments : expression

def sum1(n1,n2):
  return n1 + n2

# sum = (n1, n2)=> n1 + n2
sum = lambda n1, n2 : n1 + n2

print(sum1(1,3))
print(sum(1,3))


print(type(sum1))
print(type(sum))

# Lambda's power
def myMainFunction(y):
  return lambda x: x * y
  # x * 2


myDoubleFunction = myMainFunction(2) # lambda x: x * 2
myFourFunction = myMainFunction(4) # lambda x: x * 4


# for i in range(5):
  #print(myDoubleFunction(i+1))


# Wrapper(Main())