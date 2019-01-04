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
        self.x = None
        self.y = None

    def set_position(self, x, y):
        """
        Set the position of the table relative to the left upper corner
        :param x: X position
        :type x: int
        :param y: Y position
        :type y: int
        """
        self.x = x
        self.y = y

    def calculate_distance_to(self, table):
        """
        Calculate the distance between this table and another table. *Note*: values <= 0 are not supported
        :param table: Other table
        :type table: Table
        :return: Distance between this table and the given table
        """
        if not isinstance(table, Table):
            raise TypeError("Argument of the type 'Table' is expected.")

        if self.x is None or self.y is None:
            raise ValueError("The X and/or Y of this table are not set")

        if table.x is None or table.y is None:
            raise ValueError("The X and/or Y of the given table are not set")

        return math.sqrt(math.fabs(math.pow(table.x, 2) - math.pow(self.x, 2))
                         + math.fabs(math.pow(table.y, 2) - math.pow(self.y, 2)))
