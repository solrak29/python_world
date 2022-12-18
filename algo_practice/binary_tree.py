import pdb

DEBUG = True
def breakpoint():
    if DEBUG:
        pdb.set_trace()

class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

   def __init__(self):
        self.root = None

   def add(self, value):
       if self.root is None:
           self.root = BinaryNode(value)
           return
       else:
           self._add( self.root, value)

   def _add(self, node: BinaryNode, value):

       if value < node.value:
           if node.left:
               self._add( node.left, value)
           else:
               node.left = BinaryNode(value)
       if value > node.value:
           if node.right:
               self._add( node.right, value)
           else:
               node.right = BinaryNode(value)

   def print(self, acending: bool = True):
        if self.root is None:
           return
        node = self.root
        if acending:
            self.acend(node)
        else:
            self.decend(node)

   def acend(self, node):
        #breakpoint()
        if node.left:
            self.acend(node.left)
        print (node.value)
        if node.right:
            self.acend(node.right)

   def decend(self, node):
        if node.right:
            self.decend(node.right)
        print (node.value)
        if node.left:
            self.decend(node.left)



if __name__ == "__main__":
    value = [5,4,6,3,2,8]
    print(f'Putting in true: {value}')
    b = BinaryTree()
    for x in value:
        b.add(x)
    print('printing tree')
    b.print()
    print('--------')
    b.print(False)

