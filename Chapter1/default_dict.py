from collections import defaultdict

'''
If you want to make a dictionary that has keys that map to multiple values (a 'multi-dict')


the big feature of default dicts is that it intializes the first value so that you can focus on simply adding items. 


OrderedDict contains a doubly linked list and it is very memory intensive. Keep that in consideration. 
'''


default_dict = defaultdict()
print(type(default_dict))


nested_dict = {'name':'alexander fournier','salaries':[42500,57000,90000,120000,140000]}
salaries = [58000,98000,120000,140000,200000]

ddict = defaultdict(list)
ddict['name'].append('RedditUser')
ddict['salaries'].append(salaries)


'''


'''


