# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def add(l1: Optional[ListNode], l2: Optional[ListNode], carry:int) -> Optional[listNode]:
    if l1 is None and l2 is None and carry==0:
        return None
    
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0

    val = v1 + v2 + carry
    carry = val // 10
    val = val % 10
    next_node = add(l1.next if l1 else None,l2.next if l2 else None,carry) # inserting a new node
    return ListNode(val, next_node)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return add(l1,l2,0)