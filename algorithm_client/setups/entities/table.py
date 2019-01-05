import math


class Table:
    def __init__(self, depth, width, height):
        """
        Table
        :param depth: Length of the table
        :type depth: float
        :param width: Width of the table
        :type width float
        :param height: Height of the table
        :type height: float
        """
        self.width = width
        self.depth = depth
        self.height = height
        self.position = None

    def set_position(self, x, y):
        """
        Set the position of the table relative to the left upper corner
        :param x: X position
        :type x: int
        :param y: Y position
        :type y: int
        """
        self.position = (x, y)

    def calculate_distance_to(self, table):
        """
        Calculate the distance between this table and another table. *Note*: values <= 0 are not supported
        :param table: Other table
        :type table: Table
        :return: Distance between this table and the given table
        """
        if not isinstance(table, Table):
            raise TypeError("Argument of the type 'Table' is expected.")

        if self.position is None:
            raise ValueError("The X and/or Y of this table are not set")

        if table.position is None:
            raise ValueError("The X and/or Y of the given table are not set")

        return math.sqrt(math.fabs(math.pow(table.position[0], 2) - math.pow(self.position[0], 2))
                         + math.fabs(math.pow(table.position[1], 2) - math.pow(self.position[1], 2)))
