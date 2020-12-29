'''
problem: You have an N-Element tuple or sequence you would like to unpack into a collection of n variables


solution:
tuple unpacking

'''

test_tuple = (1,2,3)
x,y,z = test_tuple
print(x)

data = ['ACME',50, 91.1,(2012,12,21)]
name,shares,price,date = data
print(date)

name,shares,price,(year,month,date) = data
print(year)