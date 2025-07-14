# Approach (Using bit manipulation to form the decimal number)
# T.C : O(n)
# S.C : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        cur = head
        ans = 0
        while cur:
            ans = ans*2+cur.val
            cur = cur.next
        return ans