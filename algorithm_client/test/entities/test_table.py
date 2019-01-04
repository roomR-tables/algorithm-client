import unittest
from entities.table import Table


class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table(60, 60, 120)

    def test_set_position(self):
        self.table.set_position(10, 20)

        self.assertEqual(self.table.x, 10)
        self.assertEqual(self.table.y, 20)

    def test_calculate_distance_to(self):
        other_table = Table(60, 60, 120)
        other_table.set_position(0, 0)

        # Wrong argument
        self.assertRaises(TypeError, self.table.calculate_distance_to, "nope")

        # X and Y of table or not set
        self.assertRaises(ValueError, self.table.calculate_distance_to, other_table)

        self.table.set_position(10, 20)
        self.assertEqual(self.table.calculate_distance_to(other_table), 22.360679774997898)


if __name__ == '__main__':
    unittest.main()
