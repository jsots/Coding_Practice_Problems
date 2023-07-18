def canReachLeaf(root):
    if not root or root.val == 0:
        return False
    
    if not root.left and not root.right:
        return True 
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    
    return False


def leafPath(root):
    if not root or root.val == 0:
        return False
    path.append(root.val)
    
    if not root.left and not root.right:
        return True 
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    path.pop()
    
    return False