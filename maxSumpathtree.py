import sys
 
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def printPath(root, total):
    if total == 0 and root is None:
        return True
    if root is None:
        return False
    left = printPath(root.left, total - root.data)
    right= False
    if not left:
        right = printPath(root.right, total - root.data)
    if left or right:
        print(root.data, end=' ')
    return left or right
 
def getRootToLeafSum(root):
    if root is None:
        return -sys.maxsize
    if root.left is None and root.right is None:
        return root.data
    left = getRootToLeafSum(root.left)
    right = getRootToLeafSum(root.right)
    return (left if left > right else right) + root.data
 
def findMaxSumPath(root):
    total = getRootToLeafSum(root)
    print('The maximum sum is', total)
    print('The maximum sum path is ', end='')
    printPath(root, total)
 
if __name__ == '__main__':
 
    root = None
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(8)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(10)
    root.right.left.left = Node(7)
    root.right.left.right = Node(9)
    root.right.right.right = Node(5)
 
    findMaxSumPath(root)




# def _recurse_tree(parent, depth, source):
#     last_line = source.readline().rstrip()
#     while last_line:
#         tabs = last_line.count('\t')
#         if tabs < depth:
#             break
#         node = last_line.strip()
#         if tabs >= depth:
#             if parent is not None:
#                 print "%s: %s" %(parent, node)
#             last_line = _recurse_tree(node, tabs+1, source)
#     return last_line

# inFile = open("triangle.txt")
# _recurse_tree(None, 0, inFile)