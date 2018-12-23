'''<Summary>
    1. Get Current Table Positions
    2. Get Desired Table Positions
    3. Map Current Table Positions to desired table positions
    4. Desired pos - Current Pos = Directions
    5. Send directions to Control Centre

    <Summary>'''

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def Direction(self, other):
        return other - self

class Table:
    def __init__(self, id, vector2):
        self.id = id
        self.vector2 = vector2

currentTablePositions = [Vector2(4,1), Vector2(4,2). Vector2(4,4)]
desiredTablePositions = [Vector2(4,1), Vector2(4,3), Vector2(4,4)]

