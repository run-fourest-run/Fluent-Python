from collections import deque

'''
problem: You want to keep a limited history of the last few lines during iteration or during some kind of other process

solution: Keeping a limited history is perfect usecase for collections.deque. Code below performs a simple text match on a sequence of lines
and yields the matching line along with the previous n lines of context that are found


When writing code to search for items it is common to write a generator function. This decouples the processes of searching from the code that uses the results.




'''



'''
example usage of the deque below.... 


Deques are helpful to create a fixed length queue. When new items are added to the queue the oldest one is purged. See below

'''


deque1 = deque(maxlen=5)
deque1.append(1)
deque1.append(2)
deque1.append(3)
deque1.append(4)
deque1.append(5)
print(deque1)
deque1.append(6)
print(deque1)




'''
Real World example of using deque below....


'''



test_file = r'C:\Users\afournier\PycharmProjects\PythonCookbook\Chapter1\resources\deque_test.txt'


def search(lines,pattern,total_history=5):
    previous_lines = deque(maxlen=total_history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)


with open(test_file) as f:
    pattern = 'alexander'
    for line,previous_lines in search(f,pattern):
        for p_line in previous_lines:
            pass
            #print(p_line, end='')



