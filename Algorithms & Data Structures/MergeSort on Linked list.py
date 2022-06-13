from posixpath import split
from Linked_list import SinglyLinkedList

def merge_sort(SinglyLinkedList):
    """
    Sorts a linked list in ascending order
    - recursivley diivide the sorted list into sublists containing a single node
    - repeatedly merge the sublists to produce sorted sublist until one remains
    
     Returns a sorted linked  list
    """
    if SinglyLinkedList.size() == 1 or SinglyLinkedList.head is None:
        return SinglyLinkedList
    
    left_half, right_half = split(SinglyLinkedList)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)


def split(SinglyLinkedList):
    """
    Divide the unsorted list at midpoint into sublists
    """
    
    if SinglyLinkedList == None or SinglyLinkedList.head == None:
        left_half = SinglyLinkedList
        right_half = None
        
        return left_half, right_half
    else:
        size = SinglyLinkedList.size()
        mid = size // 2
        
        mid_node = SinglyLinkedList.node_at_index(mid-1)
        
        left_half = SinglyLinkedList
        right_half = Linked_list()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
    
    
def merge(left,right):
    """ 
    Merges 2 linke dlikns sorting bu data in nodes, 
    returns a new merged lists
    """
    # creatses a new linked lists that conains nodes mergif fom left and right
    
    merged = Linked_list()
    
    # add a fake head that is discarded later