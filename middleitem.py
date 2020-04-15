# Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.

# list with odd length of items
# list with even numbers
# make listnode with a value and next pointer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Singly

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        new_list = []
        while node != None:
            new_list.append(node)
            node = node.next
        length = len(new_list)
        middle_index = length // 2  
        middle_node = new_list[middle_index]
        return middle_node



    