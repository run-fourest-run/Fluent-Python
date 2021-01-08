import json


'''
Remove duplicates from sequences while maintaining order


problem: You want to eliminate duplicate values in a sequence, but preserve the order of the remaining items.


solution: If the values in the sequence are hashable, the problem can be easily solved using a set and a generator:



'''
input_file = r'C:\Users\afournier\PycharmProjects\PythonCookbook\Chapter1\resources\instagram_data\likes.json'

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def get_items(input_file):
    with open(input_file) as f:
        data = json.load(f)
        for key,val in data.items():
            if key == 'media_likes':
                users = [x[1] for x in val]
                return users



items = get_items(input_file)
sorted_items = sorted(items)
deduplicated_items = dedupe(sorted_items)
for x in deduplicated_items:
    print(x)


''' the above recipe only works if the items in the sequence are hashable. If they are unhashable 
(like in the case of dicts) you can make the following recipe change'''

'''The key is a specialty function that converts sequence items into a hashable type'''
'''to be honest I have no idea what is going on here and need to follow up on this'''
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

key = lambda d: (d['x'],d['y'])

def dedupe(items,key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

print(list(dedupe(a,key=key)))




'''Closing Notes:

If all you want to do is eliminate duplicates you can always cast the container to a set. For example:

a = [1,2,2,3,4,5]
b = set(a)
print(a)
*******
{1,2,3,4,5}
*******

However this doesn't preserve any kind of ordering. So the resulting data will be scrambeled after. The solution above
avoids this. 

'''