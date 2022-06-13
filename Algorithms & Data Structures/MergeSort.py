
from email.errors import MultipartInvariantViolationDefect
from posixpath import split


list = [54, 26,92,62,17,77,31,44,55,20]

def mergeSort(list):
    """ runs in O(kn log n)--> much more expensive
    sorts a list in ascending order
    returns a new sorted list
    
    divides: find the midpoint and divide into sublists
    Conquer: recursively sort the sublists created in previous steps
    Combine: Merges the sorted sublists in previous steps
    """
    if len(list) <=1:
        return list
    
    left_s, right_s= split(list)
    left = mergeSort(left_s)
    right = mergeSort(right_s)

    return merge(left, right)    
    
    
def split(list):
    """ 
    Takes O(k log n)
    divide the unsorted list at midpoint into sublists
    returns 2 sublists- left and right
    
    """
    left, right = 0,len(list)-1
    mid = (left + right)//2
    left = list[: mid]
    right = list [mid:]
    
    return left, right
    
def merge(left, right):
    """ runs in overall O(n) time
    merges 2 lists , sorting them in the process and returns a new merged list 
    """
    l =[]
    i = 0
    j = 0
    
    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+= 1
        else:
            left[i] >= right[j]
            l.append(right[j])
            j +=1
            
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j+= 1
    return l

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n ==1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

op = mergeSort(list)
print(verify_sorted(list))
print(verify_sorted(op))