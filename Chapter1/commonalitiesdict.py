'''
Question: you have two dictionaries and want to find out what they might have in common

'''

a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}


#find keys in common
common_keys = a.keys() & b.keys()

#find keys that are in a but not in b
keys_in_a_not_in_b = a.keys() - b.keys()
print(keys_in_a_not_in_b)
keys_in_b_not_in_a = b.keys() - a.keys()
print('the value of the variable {} is {} (it should be w)'.format(keys_in_b_not_in_a.__class__.__name__,keys_in_b_not_in_a))


'''want to make a new dictionary with certain keys removed...'''

certain_keys_removed = {key : a[key] for key in a.keys() - {'z','y'}}
for key in certain_keys_removed:
    print(key)
























'''
This section was trying to apply the above 'finding commonalaties in dicts' to 
instagram dataset
'''



'''
def get_follower_following():
    with open(connections_file) as connf:
        data = json.load(connf)
        followers = {}
        following = {}
        for key,value in data.items():
            if key == 'followers':
                followers.update(value)
            elif key == 'following':
                following.update(value)
        commonalities = followers.keys() & following.keys()
        return commonalities


def get_followers_not_following():
    with open(connections_file) as conf:
        data = json.load(conf)
        followers = {}
        following = {}
        for key,value in data.items():
            if key == 'followers':
                followers.update(value)
            elif key == 'following':
                following.update(value)
        not_following = following.keys() - followers.keys()
        return not_following

print(get_followers_not_following())'''
