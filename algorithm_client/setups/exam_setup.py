import math
from typing import List
from setups.entities.table import Table
from setups.exceptions.setup_error import SetupError


class ExamSetup:
    def __init__(self, room, tables):
        """
        Exam setup
        :param room: Instance of as single Room object
        :type room: Room
        :param tables: An array of multiple Table objects for the room
        :type tables: list[Table]
        """
        self.room = room
        self.tables = tables

        # TODO: Make this either variable or give it an appropriate unit
        self.distance_between_width = 50
        self.distance_between_length = 80

    def create_setup(self) -> List[Table]:
        """
        Calculate a setup based on the dimensions of the given room and given tables
        :return: List of tables in the correct position for this setup
        """
        # We assume that all tables have the same dimensions
        table_width = self.tables[0].width
        table_depth = self.tables[0].depth
        max_tables_width = math.floor(self.room.width / (table_width + self.distance_between_width))
        max_tables_length = math.floor(self.room.length / (table_depth + self.distance_between_length))

        if max_tables_width * max_tables_length < len(self.tables):
            raise SetupError("To many tables to create this setup")

        # Give all tables a position until there are not tables left
        current_row = 1
        tables_in_row = 0
        assigned_tables = []

        while len(self.tables) != 0:
            if tables_in_row == max_tables_width:
                current_row += 1
                tables_in_row = 0

            table = self.tables.pop()
            table.set_position(tables_in_row * (table.width + self.distance_between_width),
                               current_row * self.distance_between_length)

            assigned_tables.append(table)
            tables_in_row += 1

        return assigned_tables
