def linear_search(list, target):
    """
    returns the position where the target is found
    """
    for i in range(0, len(list)): #we want to assign values to the index
        if list[i] == target: # if the value in the list at 1 == target
            return i
    return None
    
def verify(index):
    if index is not None:
        print('Target found at Index: ', index)
    else:
        print('Target not found in list')
            
list = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(list, 12)
verify(result)

result = linear_search(list, 6)
verify(result)
