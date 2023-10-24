from collections import deque 
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        root = 0
        combined = set(leftChild+rightChild)

        for i in range(n):
            if i not in combined:
                root = i

        queue = deque([root])
        visited = set()

        while queue:
            node = queue.popleft()

            if node in visited:
                return False
            
            visited.add(node)

            if leftChild[node]!=-1:
                queue.append(leftChild[node])
            if rightChild[node]!=-1:
                queue.append(rightChild[node])


        return n == len(visited)
        