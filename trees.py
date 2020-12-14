class BST:
    """
    Create an empty BST
    """

    class Node:
        """
        Create a node class to hold the data and references to other data
        """

        def __init__(self, data):
            # set the data to be the root. Links are None
            # because they are unkown.
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        # Set the root to be None because it is empty

        self.root = None

    def insert(self, data):
        # Insert data into Tree

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, node):
        """
        Determine where to insert the data into the tree
        This uses recursion to go to the next line of the tree if
        there is not an open branch.
        """

        if data < node.data:

            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)

        elif data > node.data:

            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    # iter function to run through tree
    def __iter__(self):
        """
        Go forward through the tree
        """
        yield from self._traverse_forward(self.root)

    # traverse forward through the tree
    def _traverse_forward(self, node):
        """
        This runs through the tree on either side, and gets data until
        there is not anymore to find. It starts on the left side to get
        the smaller values, then the root value, and then the bigger
        values.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    # Runs through the tree backwards
    def __reversed__(self):
        """
        Go backward through the tree
        """
        yield from self._traverse_backward(self.root)

    # traverse backward through the tree
    def _traverse_backward(self, node):
        """
        This runs through the tree on either side, and gets data until
        there is not anymore to find. It starts on the right side to get
        the highest values, then the root value, and then the smaller
        values.
        """
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)


print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
# extra tests
tree.insert(5)
tree.insert(5)
tree.insert(5)

# given tests
tree.insert(5)
tree.insert(3)
tree.insert(7)
# After implementing 'no duplicates' rule,
# this next insert will have no effect on the tree.
tree.insert(7)
tree.insert(10)
tree.insert(1)
for x in tree:
    print(x)  # 1, 3, 5, 7, 10

print("\n=========== PROBLEM 2 TESTS ===========")
print(3 in tree)   # True
print(4 in tree)   # False
print(5 in tree)   # True
print(10 in tree)  # True
print(11 in tree)  # False
print(0 in tree)   # False

print("\n=========== PROBLEM 3 TESTS ===========")
for x in reversed(tree):
    print(x)  # 10, 7, 5, 3, 1
