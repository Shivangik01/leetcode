# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 3 conditions (positive)
# division, extras, none

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        num = 0
        node = head

        while node!=None:

            node = node.next
            num += 1

        divisions = num//k
        extras = num % k
        remaining = 0
        if num<k:
            remaining = k - extras

        node = head
        res = []

        while node!=None:

            temp_d = divisions
            curr_head = node
            res.append(curr_head)

            #print(res)

            while temp_d > 0 and node!=None:

                temp_d -= 1

                if temp_d == 0:
                    temp_new = node
                
                node = node.next
                

            if extras > 0 and node != None:
                
                temp_new = node
                node = node.next
                extras -= 1
                

            temp_new.next = None


        while remaining > 0:
            res.append(None)
            remaining -=1

        
        return res