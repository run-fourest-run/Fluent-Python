from operator import itemgetter

'''
problem: You have a list of dictionaries and you would like to sort the entries according to one or more dict. values

solution:
sorting this type of data structure is easy using the operators itemgetter function. Let's say you've queried a db table
to get the listing of the members on your website ... see below
'''


rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


rows_by_fname = sorted(rows, key= itemgetter('fname'))
rows_by_lname = sorted(rows,key=itemgetter('lname'))


'''itemgettr can also use multiple keys'''


rows_sorted_by_both_fields = sorted(rows, key=itemgetter('fname','lname'))



names = [
{"name": "Tom", "age": 10},
{"name": "Mark", "age": 5},
{"name": "Pam", "age": 7}
]



names_sorted = sorted(names,key=itemgetter('age'))
print(names_sorted)


'''rows are passed to the bul-in sorted() function, which accepts a key-word arguement key, this arguement is expected
to be a callable that accepts a single item from rows as input and returns a value that will be used as the basis for sorting'''



'''Itemgettr functionality is sometimes replaces with a lambda function'''


names_sorted = sorted(names,key=lambda row: row['name'])
print(names_sorted)


'''this recipe can also be applied to minimum and maximum functions - min,max'''

minimum = min(names,key=lambda row: row['age'])
print(minimum)

maximum = max(names,key=lambda row:row ['age'])
print(maximum)
minimum= min(names , key = lambda row: row['age'])
print(minimum)