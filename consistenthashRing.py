class SubTree(object):

    '''
    A class that implements a subtree in our binary search tree. This subtree can be either a node, a node with leaf nodes, or a node with other other subtrees as children. 

    Methods for removal and insertion are defined here. Lookup is not provided as we only care about that when we have access to a dedicated root node. 
    '''

    def __init__(self, value, left=None, right=None):

        '''
        @param: value [Any]: The raw value you wish to insert. Must implement comparison.
        @param: left, right [Node]: Left and right children of this node.
        '''

        self.value, self.key = value, hash(value)
        self.left, self.right = left, right
How to handle insertion:

    def add_child(self, value):

        ''' 
        Recursively add a child node with the defined value.
        Duplicate values are excluded in this tree.
        '''

        key = hash(value)

        if key == self.key:
           return 

        if key > self.key:

            if self.right is None:
                self.right = SubTree(value)
            else:
                self.right.add_child(value)

        if key < self.key:

            if self.left is None:
                self.left = SubTree(value)
            else:
                self.left.add_child(value)
How to handle deletion (here, find_in_order_successor() just finds the next higher-valued key):

    def remove_value(self, value):
        '''
        Removes a value from this node and its subtree. 
        Returns the new node that should take the place of the node 
        that was removed.
        '''

        key = hash(value)

        if key == self.key:

            # if leaf node, remove oneself
            if self.left is None and self.right is None:
                return None

            # the following two cases return whichever child node is 
            # extant for a one-child parent.

            if self.left is None and self.right is not None:
                return self.right

            if self.right is None and self.left is not None:
                return self.left

            # case where neither left or right child is empty
            if self.right is not None and self.left is not None:
                # copy the value of the first in-order successor, 
                # then delete the first in-order successor node.
                self.value = self._find_in_order_successor()
                self.right = self.right.remove_value(self.value)
                return self
        else:
             if self.left is not None:
                 self.left = self.left.remove_value(value)
             if self.right is not None:
                 self.right = self.right.remove_value(value)
             return self #
Now that we have a bare basic binary search tree, let’s finally implement our hash ring:

class ConsistentHashRing(object):

    ''' 
    A wrapper around the SubTree class that lets you manipulate the whole tree at once.
    This class provides access to the root node, and enables you to search the tree
    for the closest match to a value. Iteration and length methods return all stored 
    values in the tree, however.
    Values added to this ConsistentHashRing _must_ be hashable. 
    '''

    def __init__(self, value=None):
        self.head = None if value is None else SubTree(value)
Addition and deletion have already been implemented for self.head – we just need to call those appropriately:

    def add_node(self, value):

        ''' Add a value to the tree as a whole. '''

        if self.head is None:
           self.head = SubTree(value)
        else:
           self.head.add_child(value)

    def remove_node(self, value):

        ''' 
        Remove a value from the tree. 
        Only exact matches may be removed - values not in the tree 
        are ignored. 
        '''

        if self.head is None:
            return 

        self.head = self.head.remove_value(value)
The meat of the matter, however, lies in how we find the nearest upper neighbour:

    def find_best_match(self, value):

        '''
        Search for closest match - if exact value exists, it shall return that value, otherwise it will return the closest
        value. If the tree is empty, it returns None.
        Note that 'closest match' here translates to first bigger value than value passed in as parameter here. If an exact
        match is found, it returns that. 
        '''

        key = hash(value)
        current_node = self.head
        best_match, best_match_key = None, float("inf")

        # if tree is empty, return None
        if not self.head:
            return None

        # if tree is not empty, walk through the binary search tree, and update the best_match to reflect the closest but 
        # larger value encountered.

        while current_node is not None:

            # exit if exact match is found, returning that value
            if current_node.key == key:
                return current_node.value

            # if number is bigger, check if it is closer to our target value than the last number, and choose to update
            # accordingly
            if current_node.key > key:

                best_match = current_node.value if abs(current_node.key - key) < abs(best_match_key - key) else best_match
                best_match_key = hash(best_match)

                current_node = current_node.left
                continue

            if current_node.key < key:
                current_node = current_node.right
                continue

        # best_match can still be None if all values in the BST are smaller than the submitted value. In that case,
        # we always return the smallest value in the BST, in line with the principles behind consistent hashing. 

        if best_match:
            return best_match
        else:
            # will always return the smallest value in the BST
            return self.head._find_minimum_subtree_child_value()
