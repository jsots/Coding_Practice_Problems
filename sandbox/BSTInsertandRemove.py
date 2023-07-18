def insert(root, val):
    # Base case, root is null/None
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    
    return root


# Find minimum in a BST (will be on the left):

def findMinValue(root):
    curr = root

    while curr and curr.left:
        curr = curr.left
    
    return curr