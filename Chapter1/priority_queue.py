import heapq

'''
Problem: Implement a queue that sorts items by a given priority and always returns the item with the highest priorty after each pop operation 

'''


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r})'.format(classname,self.name)

queue = PriorityQueue()
item1 = Item('work')
item2 = Item('menthal_health')
item3 = Item('physical_health')
item4 = Item('nutrition')


item1 = (1,Item('work'))
item2 = (2,Item('mental_Health'))
item3 = (2,Item('physical health'))
print(item1<item2) # will return true
print(item3<item2)



'''

queue.push(item1,1)
queue.push(item2,3)
queue.push(item3,2)
print(queue.pop())
print('#####################')
queue.push(item4,1)
print(queue.pop())
print(queue.pop())
print('####################')
print(queue.pop())
print(queue.pop())
'''