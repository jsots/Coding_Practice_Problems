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

# Need the above to aid the function below, removing.

def remove(root, val):
    if not root:
        return None
    
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    
    return root