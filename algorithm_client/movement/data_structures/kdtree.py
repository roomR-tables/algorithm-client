from typing import List, Callable
from movement.exceptions.kdtree_error import KdTreeError, KdTreeNotFoundError
from movement.data_structures.kdnode import KdTreeNode


class KdTree:
    def __init__(self, dimensions, start_dimension):
        """
        KD tree
        :param dimensions: Amount of dimensions
        :type dimensions: int
        :param start_dimension: Dimension of the root node
        :type start_dimension: int
        """
        self.dimensions = dimensions - 1
        self.start_dimension = start_dimension - 1
        self.root = None

    def insert(self, value_to_insert, compare_function: Callable[[any, any, int], int]):
        """
        Insert a new value into the KD tree
        :param value_to_insert: Value to insert; Must be a tuple with the amount of values equal to the amount of
        dimensions
        :param compare_function: Function to compare values against each other;
        :type compare_function: lambda; returns: -1 if value is < node value, 0 is value == node value, 1 if value > node value
        :return:
        """
        if self.root is None:
            self.root = KdTreeNode(value_to_insert)
        else:
            self._insert(value_to_insert, compare_function, self.root, self.start_dimension)

    def _insert(self, value, compare_function, curr_node, curr_dimension):
        """
        Private recursive insertion method
        :param value: Value to insert
        :type value: tuple
        :param compare_function: Function to compare values against each other;
        :type compare_function: lambda; returns: -1 if value is < node value, 0 is value == node value, 1 if value > node value
        :param curr_node: Current node in the tree
        :type curr_node: KdTreeNode
        :return:
        """
        if compare_function(value, curr_node.value, curr_dimension) <= 0:
            if curr_node.left is None:
                curr_node.left = KdTreeNode(value)
            else:
                next_dimension = 0 if curr_dimension + 1 > self.dimensions else curr_dimension + 1
                self._insert(value, compare_function, curr_node.left, next_dimension)
        else:
            if curr_node.right is None:
                curr_node.right = KdTreeNode(value)
            else:
                next_dimension = 0 if curr_dimension + 1 > self.dimensions else curr_dimension + 1
                self._insert(value, compare_function, curr_node.right, next_dimension)

    def find(self, value, search_func: Callable[[any, KdTreeNode, int], int]) -> KdTreeNode:
        """
        Find an exact value in the KD tree
        :param value: Value to search for
        :type value: tuple
        :param search_func: Function to compare values against each other
        :type search_func: lambda; returns: -1 if value is < node value, 0 is value == node value, 1 if value > node value
        :return:
        """
        if type(value) is not tuple:
            raise TypeError("The given value is not a tuple")

        if len(value) != self.dimensions + 1:
            raise ValueError("The given value does not have the same dimensions as the KD tree supports")

        if self.root is None:
            raise KdTreeError("The KD tree is empty")

        curr_node = self.root
        curr_dimension = self.start_dimension
        found_node = None

        while found_node is None and curr_node is not None:
            compare_result = search_func(value, curr_node, curr_dimension)
            next_dimension = 0 if curr_dimension + 1 > self.dimensions else curr_dimension + 1

            if compare_result == 0:
                found_node = curr_node
            elif compare_result == -1:
                curr_node = curr_node.left
                curr_dimension = next_dimension
            elif compare_result == 1:
                curr_node = curr_node.right
                curr_dimension = next_dimension

        if found_node:
            return found_node
        else:
            raise KdTreeNotFoundError()

    def traverse_left(self) -> List[any]:
        return self._traverse_left(self.root)

    def _traverse_left(self, curr_node) -> list:
        res = []

        if curr_node:
            res = self._traverse_left(curr_node.left)
            res.append(curr_node.value)
            res = res + self._traverse_left(curr_node.right)

        return res
