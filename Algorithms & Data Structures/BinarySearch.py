list = [1,2,3,4,5,6,7,8,9]
target = 3


def binary_search(list, target):
    first, last = 0, len(list) - 1
    
    while first <= last:
        midpoint= (first + last)// 2 # to get the index of the middle index
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint  - 1
            
    return None

print(binary_search(list, target))