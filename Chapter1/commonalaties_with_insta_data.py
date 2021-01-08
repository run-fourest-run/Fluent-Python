import json

'''
a note on dictionaries:

they are simply a mapping between a set of keys and values. The Keys() method of a dictionary returns a keys-view object
that exposes the keys. A little known feature of key views is that they support common set operations such as unions/instersections/
and differences. 

the items() method of a dictionary returns an items view object consisting of (key,value) pairs. The object supports similar set 
operations and can be used to perform operations such as finding out which key-value pairs two dictionaries have in common. 






'''


input_file = r'C:\Users\afournier\PycharmProjects\PythonCookbook\Chapter1\resources\instagram_data\connections.json'


def get_connections_minus_person(connections_file,person_name=None):
    with open(connections_file) as f:
        data = json.load(f)
        followers = {}

        for key,val in data.items():
            if key == 'followers':
                followers.update(val)

        final_dict = {key:followers[key] for key in followers.keys() - {person_name}}
        return final_dict



for key in get_connections_minus_person(connections_file=input_file,person_name='ll.smns'):
    print(key)



