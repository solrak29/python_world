'''
This module will provide the code that will merge two binary trees
but suming the nodes that are in the same place of the tree
'''

from binary_tree import BinaryTree, BinaryNode

def recurse_and_merge( b1, b2):
    if b1.left and b2.left:
        b1.left.value += b2.left.value
        recurse_and_merge(b1.left, b2.left)
    elif b2.left:
        b1.left = b2.left
    if b1.right and b2.right:
        b1.right.value += b2.right.value
        recurse_and_merge(b1.right, b2.right)
    elif b2.right:
        b1.right = b2.right


if __name__ == "__main__":
    data1 = [5,4,6,3,2,8]
    data2 = [7,1,6,3,2,8]
    b1 = BinaryTree()
    b2 = BinaryTree()
    for d in data1:
        b1.add(d)
    for d in data2:
        b2.add(d)

    b1.print()
    print('-------')
    b2.print()
    b1.root.value += b2.root.value
    recurse_and_merge(b1.root, b2.root)
    print('******')
    b1.print()


