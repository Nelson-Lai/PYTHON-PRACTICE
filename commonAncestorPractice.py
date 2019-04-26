class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent

def commonAncestor(node1,node2):
    nodeSet1 = set()
    node = node1
    while True:
        nodeSet1.add(node.val)
        if node.parent == None:
            break
        node = node.parent
    node = node2

    while True:
        if node.val in nodeSet1:
            return node.val
        if node.parent == None:
            break
        node = node.parent
    return 'No Common Ancestors'



node1 = Node(1,None)
node2 = Node(2,node1)
node3 = Node(3,node1)
node4 = Node(4,node2)
node5 = Node(5,node2)
node6 = Node(6,node5)
node7 = Node(7,node5)

print(commonAncestor(node7,node3))

'''
1
|\
2 3
|\
4 5
  |\
  6 7
'''
