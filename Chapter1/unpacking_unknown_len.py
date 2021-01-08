


import math

'''
problem: You need to unpack N elements from an iterable, but the iterable my be longer than N elements,
causing a "Too many values to unpack" exception


solution: Python "Star expressions" ... similar to *args and **kwargs
'''

'''

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

sales_numbers = [120000,24442,343242,525252]
*trailing_quarters,curret_quarter  = sales_numbers
print(*trailing_quarters)


SE = ['alexander','joe','david','alan']
se1,*se,se2 = SE
print(*se)

'''




'''
Extended iterable unpacking is tailor made for unpacking iterables of unknown or arbitrary length.
Oftentimes these iterables have some known component or pattern in their construction. 

example: Everything after element 1 is a phone number



'''


records = [('employee_fullname','Alexander Fournier'),('employee_firstname','Joeseph','employee_lastname','Chimilewski'),('employee_firstname','Anthony','employee_middlename','Ricky','employee_lastname','Fazion')]

def get_fullname(x):
    return x

def get_fullname_firstlast(firstnameval,lastnameid,lastnameval):
    if lastnameid == 'employee_lastname':
        return firstnameval + ' ' + lastnameval

def get_fullname_firstmiddle_last(firstnameval,middlenameid,middlenameval,lastnameid,lastnameval):
    if middlenameid == 'employee_middlename' & lastnameid =='employee_lastname':
        return firstnameval + ' ' + middlenameval + ' ' + lastnameval

for identifier ,*rest in records:
    if identifier == 'employee_fullname':
        print(get_fullname(*rest))
    elif identifier == 'employee_firstname':
        print(get_fullname_concated(*rest))
