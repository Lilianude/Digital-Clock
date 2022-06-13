# def recursive_binary_search(list, target):
#     if len(list) == 0 :
#         return False
#     else:
#         midpoint = (len(list))//2
        
#         if list[midpoint] == target:
#             return True
#         else: 
#             if list[midpoint]< target:
#                 return recursive_binary_search(list[midpoint+1 :], target)
#             else:
#                 return recursive_binary_search(list[: midpoint], target)
            
            
# def verify(index):
#     if index in list:
#         print('Target found ', result)
#     else:
#         print("Target not found ", result)
    
# list = [1,2,3,4,5,6,7,8,9,10]
# result = recursive_binary_search(list, 12)
# verify(result)

# result = recursive_binary_search(list, 8)
# verify(result)

# linked lists







class Node:
    '''
    An object for storing  a singl enode of a linked list.
    Models 2 attributes - data and the link to the next node in the list
    '''
    data = None
    next_node = None
    
    def __init__(self, data) :
        self.data = data
        
        
    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data # the % sign replaces data with what you want to replace it with.
    
class LinkedList:
    '''
    Single linked list '''
    
    def __init__(self):
        self.head = None
        
            