class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform Postorder traversal on the tree
def preOrder(node):
	if not node:
		return
	
	print (node.data),
	preOrder(node.left)
	preOrder(node.right)
 
 
# Function to construct balanced BST from the given sorted list
def construct(keys, low, high, root):
 
    # base case
    if low > high:
        return root
 
    # find the middle element of the current range
    mid = (low + high) // 2
 
    # construct a new node from the middle element and assign it to the root
    root = Node(keys[mid])
 
    # left subtree of the root will be formed by keys less than middle element
    root.left = construct(keys, low, mid - 1, root.left)
 
    # right subtree of the root will be formed by keys more than the middle element
    root.right = construct(keys, mid + 1, high, root.right)
 
    return root
 
 
# Function to construct balanced BST from the given unsorted list
def constructBST(keys):
 
    # sort the keys first
    keys.sort()
 
    # construct a balanced BST and return the root node of the tree
    return construct(keys, 0, len(keys) - 1, None)
 
 
if __name__ == '__main__':
 
    # input keys
    keys = [-5,-10,0,15,20,100,-100]
 
    # construct a balanced binary search tree
    root = constructBST(keys)
 
    # print the keys in an inorder fashion
    preOrder(root)