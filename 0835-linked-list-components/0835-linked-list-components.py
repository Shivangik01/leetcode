# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        res = 0
        node = head

        while node!=None:

            if node.val in nums and (node.next==None or node.next.val not in nums):
                res+=1
    
            
            node=node.next

        return res