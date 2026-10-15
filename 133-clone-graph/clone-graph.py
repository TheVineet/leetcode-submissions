"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {} #Old node : New Node
        def dfs(node, visit):
            if node in visit:
                return

            if node not in oldToNew:
                newNode = Node(node.val)
                oldToNew[node] = newNode
            
            newNode = oldToNew[node]

            visit.add(node)
            
            for child in node.neighbors:
                if child not in oldToNew:
                    newChild = Node(child.val)
                    oldToNew[child] = newChild
                newChild = oldToNew[child]
                newNode.neighbors.append(newChild)
                dfs(child,visit)
            
            return
        dfs(node,set())
        return oldToNew[node]
            


        