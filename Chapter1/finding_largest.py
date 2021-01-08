import heapq

'''
problem: 
You want to find the largest or smallest Nth item in a collection

solution:
use nlargest() or nsmallest() from the heapq library

'''



'''basic example'''





collection = [124,2442,353,3535,243,5351,9999,100000,1000000]
three_largest = heapq.nlargest(3,collection)
three_smallest = heapq.nsmallest(3,collection)



'''harder example (using keys)'''

salesengineers = [{'name':'alexander fournier','salary':125},{'name':'Joe Chimilewski','salary': 130}, {'name':'Anthony Fazio', 'salary':150}]



for engineer in salesengineers:
    for key,value in engineer.items():
        pass

three_largest = heapq.nlargest(2,salesengineers,lambda x: x['salary'])
three_smallest = heapq.nsmallest(2,salesengineers,lambda x: x['salary'])



portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]


cheap_stocks = heapq.nsmallest(3,portfolio,lambda share: share['price'])
for stock in cheap_stocks:
    for key,value in stock.items():
       if key == 'name' or key == 'price':
           pass
           #print(key,value)


'''
This solution works best if the sample of n Largest or n Smallest is small in quantity compared to the relative size of the list. 



'''


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
