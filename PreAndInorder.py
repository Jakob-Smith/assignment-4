import math


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Traversal:

    inOrderList = []
    preOrderList = []

    def inOrder(self, root):
        # escape if no root
        if root is None:
            return
        else:
            # traverse left nodes
            x = (self.inOrder(self, root.left))
            # add to list if the input was not 'null'
            if x is not None:
                self.inOrderList.append(x)
            # add to list if the root is not 'null'
            y = root.val
            if y is not None:
                self.inOrderList.append(y)
            # traverse right nodes
            z = (self.inOrder(self, root.right))
            if z is not None:
                self.inOrderList.append(z)

    def preOrder(self, root):
        # escape if root is none
        if root is None:
            return
        y = root.val
        # if the root is not None, add it to the list
        if y is not None:
            self.preOrderList.append(y)
        # visit left nodes
        if root.left is not None:
            self.preOrder(self, root.left)
        # visit right nodes
        if root.right is not None:
            self.preOrder(self, root.right)


root = []
placeHolder = 0
user = 0
print("Type \"Done\" to finish \n")

while user is not 'Done':
    user = input("Enter an integer: ")
    if user == "Done":
        break
    if user == "null":
        root.append(Node(None))
    else:
        root.append(Node(user))

max = len(root) - math.pow(2, (math.log2(len(root) + 1) - 1))

while placeHolder < max:
    root[placeHolder].left = root[2 * placeHolder + 1]
    root[placeHolder].right = root[2 * placeHolder + 2]
    placeHolder += 1

test = Traversal
test.preOrder(test, root[0])
test.inOrder(test, root[0])

print(test.inOrderList)
print(test.preOrderList)






