from typing import List
from movement.data_structures.kdtree import KdTree
from setups.entities.table import Table


class Movement:
    def __init__(self, old_setup: List[Table], new_setup: List[Table]):
        """
        Movement
        :param old_setup: Old setup to move from
        :type old_setup: list[Table]
        :param new_setup: New setup to move to
        :type new_setup: list[Table]
        """
        self.old_setup = old_setup
        self.new_setup = new_setup

    def convert_tables_to_tree(self, setup) -> KdTree:
        """
        Convert a given table setup to aan 2D-tree
        :param setup: Setup to convert
        :type setup: list[Table]
        :return: 2D-tree
        """
        tree = KdTree(dimensions=2, start_dimension=1)

        for table in setup:
            tree.insert(table, lambda t, node_t, dimension: -1 if t.position[dimension] <= node_t.position[dimension] else 1)

        return tree

    def find_new_tables(self) -> List[(Table, Table)]:
        """
        Find for each "new" table the closest "old" table
        :return: List[tuple]; (old, new)
        """
        old_and_new_table = []
        old_table_tree = self.convert_tables_to_tree(self.old_setup)

        def search_func(table, node, dimension):
            if table.position == node.value.position or node.value.position[dimension] > table.position[dimension]:
                return 0
            elif table.position[dimension] <= node.value.position[dimension]:
                return -1
            else:
                return 1

        for new_table in self.new_setup:
            old_table = old_table_tree.find(new_table.position, search_func).value
            old_and_new_table.append((old_table, new_table))

        return old_and_new_table
