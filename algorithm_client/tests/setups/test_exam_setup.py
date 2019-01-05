import unittest
from exceptions.setup_error import SetupError
from setups.exam_setup import ExamSetup
from setups.entities.room import Room
from setups.entities.table import Table


class TestExamSetup(unittest.TestCase):
    def setUp(self):
        tables = [
            Table(60, 60, 120),
            Table(60, 60, 120),
            Table(60, 60, 120),
            Table(60, 60, 120),
            Table(60, 60, 120),
            Table(60, 60, 120),
            Table(60, 60, 120),
            Table(60, 60, 120),
            Table(60, 60, 120),
            Table(60, 60, 120)
        ]
        self.setup = ExamSetup(Room(600, 300), tables)

    def test_create_setup(self):
        # overwrite the room to create and invalid setup
        self.setup.room = Room(120, 120)
        self.assertRaises(SetupError, self.setup.create_setup)

        # Reset room dimensions
        self.setup.room = Room(600, 300)

        calculated_setup = list(map(lambda t: (t.x, t.y), self.setup.create_setup()))
        expected_setup = [(0, 80), (110, 80), (220, 80), (330, 80), (440, 80), (0, 160), (110, 160), (220, 160),
                          (330, 160), (440, 160)]

        self.assertEqual(calculated_setup, expected_setup)


if __name__ == '__main__':
    unittest.main()
