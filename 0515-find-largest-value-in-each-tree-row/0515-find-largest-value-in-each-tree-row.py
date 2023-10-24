# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs store levels and max of them
from collections import defaultdict
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        maximum = defaultdict(lambda : float('-inf'))
        
        queue = [(root,0)]

        while queue:
            curr = queue.pop(0)

            node = curr[0]
            level = curr[1]


            if node!=None:
                maximum[level] = max(maximum[level],node.val)
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))


        return maximum.values()

    
        