from collections import Counter
import json
import heapq

'''problem:
you have a sequence of items and you'd like to determine the most frequently occuring items in the sequence

the collections.Counter class is designed for just such a problem. It even comes with the most handy most_common() method




'''


words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
morewords = ['why','are','you','not','looking','in','my','eyes']

for word in morewords:
    word_counts = Counter(words)
    word_counts[word] += 1





'''alternatively you can use the .update function on word_coutns'''

word_counts = Counter(words)
word_counts.update(morewords)




# print(f'the word count is {word_counts}')



'''You can also use set operations on the Counter object'''

word_counts = Counter(words)
more_word_counts = Counter(morewords)
total_word_counts = word_counts + more_word_counts
# print(total_word_counts)


'''Let's try with real life example'''
'''Problem: Find the counts of likes in likes.json'''

file = r'C:\Users\afournier\PycharmProjects\PythonCookbook\Chapter1\resources\instagram_data\likes.json'

with open(file) as f:
    data = json.load(f)
    for x in data:
        print(x)


def likes_counter(file,like_type=None):
    with open(file) as f:
        data = json.load(f)
        records_slice = slice(1,2)
        likes = [record[records_slice] for record in data[like_type]]
        final_likes = []
        for layer1 in likes:
            for layer2 in layer1:
                final_likes.append(layer2)
        aggregate_likes = Counter(final_likes)
        return aggregate_likes



total_count = likes_counter(file,like_type='media_likes')



