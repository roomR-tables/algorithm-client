import unittest
from movement.data_structures.kdtree import KdTree
from movement.exceptions.kdtree_error import KdTreeError, KdTreeNotFoundError


class TestKdTree(unittest.TestCase):
    def setUp(self):
        values_to_insert = [
            (100, 500),
            (200, 500),
            (300, 500),
            (400, 500),
            (100, 400),
            (300, 400),
            (400, 400),
            (100, 200),
            (200, 200),
            (300, 200),
            (400, 200)
        ]
        root_value = (200, 400)

        tree = KdTree(dimensions=2, start_dimension=2)
        tree.insert(root_value, lambda value, node_value, dimension: -1 if value[dimension] <= node_value[dimension] else 1)

        for value in values_to_insert:
            tree.insert(value, lambda value, node_value, dimension: -1 if value[dimension] <= node_value[dimension] else 1)

        self.tree = tree

    def test_insert(self):
        # Try to insert invalid data
        self.assertRaises(TypeError, self.tree.insert, "nope", lambda v, nv: -1)
        self.assertRaises(ValueError, self.tree.insert, (100, 200, 300), lambda v, nv: -1)

        # Traverse the tree and compare to the expected results
        traverse_result = self.tree.traverse_left()
        expected_results = [(100, 200), (100, 400), (300, 200), (400, 200), (200, 200), (400, 400), (300, 400),
                            (200, 400), (100, 500), (300, 500), (400, 500), (200, 500)]

        self.assertEqual(traverse_result, expected_results)

    def test_search(self):
        def search_func(value, node, dimension):
            if value == node.value:
                return 0
            elif value[dimension] <= node.value[dimension]:
                return -1
            else:
                return 1

        # Search both left and right
        self.assertEqual(self.tree.find((300, 500), search_func).value, (300, 500))
        self.assertEqual(self.tree.find((200, 200), search_func).value, (200, 200))

        # Search non existing value
        self.assertRaises(KdTreeNotFoundError, self.tree.find, (0, 0), search_func)

        # Search on empty tree
        self.tree.root = None
        self.assertRaises(KdTreeError, self.tree.find, (300, 500), search_func)


if __name__ == '__main__':
    unittest.main()
