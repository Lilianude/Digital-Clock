# if 10 == "10":
#     print('a')
# elif 'bag' > 'apple' and 'bag' > 'cat':
#     print('b')
# else:
#     print('c')
    
# for number in range(1, 10, 2):
#     print('You win!!', number, number *'.')

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# for x in [1,2,3,4]:
#     print (x)

#While Loop

# number  = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ''
# while command.lower() != 'quit':
#     command = input('>> ')
#     print("ECHO", command)

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print (number)
# print(f'We have {count} even numbers')

# Functions
# types of functions
# the ones that perform a task
# the ones that return a value

# def greet (name):
#     print (f'Hi {name')
    
    
# def get_name(name):
#     return f"Hi {name}"


# message = get_name('Lilian')
# file = open("content.txt","w")
# file.write(message)

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
        
        
# print('Start')        
# print(multiply(2,3,4,5))

# def save_user(**user):
#     print(user["id"])
    
    
# # save_user(id =1, name ='Lilian', age = 30)

# # Function for the Fizz-Buzz.

# def fizz_buzz(input):
#     if (input % 5 == 0) and (input % 3 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return 'Fizz'    
#     if input % 5 == 0 :
#         return 'Buzz'
#     return input
    
# print (fizz_buzz(7))
        
        
# # Unpacking of a List
# numbers = [1,2,3,4,4,4,4,4,9]
# # to unpack this you can say
# first, *other, last = numbers
# print(first, last)
# print(other)

# # Enumerate is iterable but prints a tuple
# # letters = ['a', 'b', 'c']
# # items = (0,'a')
# # index, letter = items
# # for index, letter in enumerate(letters):
# #     print(index, letter)
    
    
# # letters = ["a", "b", "c"]
# #  # add
# # letters.append("d")
# # print(letters)

# # Sorting Lists
# # items = [
# #     ("Product1", 10),
# #     ("Product2", 9),
# #     ("Product3", 12),
# # ]

# # # def sort_item(item):
# # #     return item[1]


# # # Use if lambda function to write anonymous functin
# # # items.sort(key=lambda parameter=expression)

# # items.sort(key=lambda item:item[1])
# # print (items)

# # Map Function
# # items = [
# #     ("Product1", 10),
# #     ("Product2", 9),
# #     ("Product3", 12),
# # ]

# # # prices =[]
# # # for item in items:
# # #     prices.append(item[1])

# # # print(prices)

# # # better way to do this, use  MAP function
# # x = map(lambda item: item[1], items)
# # for item in x:
# #  print(item)

# # Filter function

# # items = [
# #     ("Product1", 10),
# #     ("Product2", 9),
# #     ("Product3", 12),
# # ]

# # filtered = list(filter(lambda item: item[1]>= 10, items))

# # List Comprehension

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]
# # lambda function
# prices = list(map(lambda item: item[1], items))
# #list comprehension format [expression for item in items] for Mapping
# prices = [item[1]for item in items]
# # Lambda function
# filtered = list(filter(lambda item: item[1]>= 10, items))
# # List compression for filtering lists. filtered  [expression for item in items if item > xxx]

# filtered = [item for item in items if item[1] >= 10]

# Zip function
# list1 =[1,2,3]
# list2 = [10,20,30]

# print(list(zip("abc", list1,list2)))

# QUEUES
# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# queue.popleft()
# print(queue)
# if not queue:
#     print('empty')

# Tuples
# point =(1,2) + (3,4)
# point1 = (1, 2) * 3
# pointer = (1, 2, 3)
# x,y,z = pointer
# if 10 in pointer: 
#     print('exists')

# Swapping variables
# x= 10
# y =11
# x,y = y,x
# print("x", x)
# print("y", y)

# To use Arrays you do
# from array import array
# numbers = array("i" [1, 2, 3])
# numbers [0] = 7 
# in arrays every typecode shoud be an integer.

# SET - is an unordered collection with no duplicates

 #numbers =[1,2,2,3,3,3,5,6,7]
#first = set(numbers)
#second ={1,3,5}
#print(first | second) # union of 2 sets
#print(first & second) # intersection of 2 sets
#print(first - second) # difference of 2 sets
#print(first ^ second) # symmetric difference, return the items with in the frist or second set but not both

# DICTIONARIES- a collection of Key value pairs
# point = {"x": 1, "y":2}
# things = dict(x=1,y=2)
# things["x"] =10
# things["z"] =20
# if "a" in things:
#     print(things["a"])
# print(things.get("a", 0))

# del things["x"]
# print(things)

# for key in things:
#     print(key,things[key])

# DICTIONARIES COMPREHENSIONs
# values = []
# for x in range(5):
#     values.append(x * 2)
#     print (values)

# values2 = {x: x *2 for x in range(5)}
# print(values2)


# # Generator Expressions
# from sys import getsizeof

# values1 = [ x *2 for x in range(10)]
# for x in values:
#     print(values1)
    
# vales =[*range(5), *"Hello"] # the * is the unpacking operator
# Program to find out how may times a character was repeated

from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
#pprint(char_frequency, width=1)
char_frequency_sorted = (sorted(char_frequency.items(),
                        key=lambda kv:kv[1],
                        reverse=True))
print (char_frequency_sorted[0]) # returns the highest number which is the firstitem in the list