class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None:
        return '#'
    
    return str(root.val) + ',' + serialize(root.left) + ',' + serialize(root.right)

def deserialize(data):
    data = data.split(',')

    return _deserialize(data)

def _deserialize(data):
    if len(data) == 0:
        return None

    val = data.pop(0)

    if val == '#':
        return None

    node = Node(val)

    node.left = _deserialize(data)
    node.right = _deserialize(data)

    return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
