'''problem:
Your program has become an unreadable mess of hardcoded slice indices you want to clean up

solution:
Suppose you have some code that is pulling specific data fields out of a record string with fixed fields (e.g
'''

record = '....................100 .......513.25 ..........'
# cost = int(record[20:23] * float(record[31:37]))



'''instead you could use the following recipe


why use it? 
basically this allows you to replace the numbers in the slices making it more readable
'''

shares = slice(20,23)
print(f'the ammount of shares = {record[shares]}')
price = slice(31,37)
# cost = int(record[shares] * float(record[price]))


#confusing
test_shares = int(record[20:23])
# morereadable
test_cost = float(record[price])




'''
of general note: Avoid hardcoding index values ... leads to readability and maintance mess. For example, 
if you come back to the code a year later, you'll look at it and wonder what they were thinking when they wrote it.



built-in slice() uses a slice object that can be used anywhere a slice is allowed.
'''

items = [0,1,2,3,4,5,6,7,8,9,10]
first_slice = slice(1,5)
items_firt_slice = items[first_slice]
print(items_firt_slice)



'''
You can also map a slice onto a sequence of a specific size by using it's indices(size) method. This returns a tuple:
(start,stop,step) where all values have been suitably limited to fit within the bounds
'''

first_name_slice = slice(0,4)
last_name_slice = slice(5,13)
fullname_string = 'alex fournier'
firstname_string  = fullname_string[first_name_slice]
lastname_string = fullname_string[last_name_slice]
print(firstname_string,lastname_string)


'''
since it's an object you can access it's attributes pretty easily
'''

print([x*100 for x in '#'])
print('slice attributes')
print([x*100 for x in '#'])

print(first_name_slice.start,first_name_slice.stop)

'''

you can map a slice onto a sequence of a specific size by using indices(size) method

'''



s = 'HelloWorld'
a = slice(10,50,2)
test = a.indices(len(s))
print(test)
for i in range(*a.indices(len(s))):
    print(s[i])
