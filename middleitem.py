# Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.

# list with odd length of items
# list with even numbers
# make listnode with a value and next pointer


# Definition for singly-linked list.

oddList = [1,2,3,4,5,6,7]
evenList = [1,2,3,4,5,6,7,8]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Singly

# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         node = head
#         new_list = []
#         while node != None:
#             new_list.append(node)
#             node = node.next
#         length = len(new_list)
#         middle_index = length // 2  
#         middle_node = new_list[middle_index]
#         return middle_node


# Doubly

class Solution: 
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        node_total = 0
        middle_node = 
        while node != None:
            node = node.next
            node_total += 1

        middle_index = node_total // 2
        new_node = head
        for i in range(0, middle_index + 1):
            new_node = new_node.next
            middle_node = new_node 
            return middle_node
    