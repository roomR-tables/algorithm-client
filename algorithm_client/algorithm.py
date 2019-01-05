'''<Summary>
    Sources:
    https://www.quora.com/What-algorithms-do-good-line-follower-robots-use

    1. Get Current Table Positions
    2. Get Desired Table Positions
    3. Merge Sort Current Tale Positions from bottom left to top right
    4. Merge Sort Desired Tabble positions from bottom left to top right
    5. Map Current Table Positions to desired table positions
    6. Desired pos - Current Pos = Directions
    7. end directions to Control Centre
    <Summary>'''

#   2 dimensional coordinate class.
class V2:
    #   Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #   Overload plus
    def __add__(self, other):
        return V2(self.x + other.x, self.y + other.y)
    #   Overload minus
    def __sub__(self, other):
        return V2(self.x - other.x, self.y - other.y)
    #   Get V2 Coordinates needed to go from self to other
    def Coordinates(self, other):
        return other - self
    #   Get the distance from self to other in a single value
    def Distance(self, other):
        a = self.x + self.y
        b = other.x + other.y
        return abs(a - b)
    #   Sort a Vector2 list from small to large on X and than Y
    @staticmethod
    def MergeSort(VList):

        #   Stop when 1 item is left
        if len(VList) <= 1:
            return VList

        #Split lists in half
        l1 = V2.MergeSort(VList[0:int(len(VList) / 2)])
        l2 = V2.MergeSort(VList[int(len(VList) / 2):len(VList)])
        result = []

        #Sort by comparing y then x
        while len(l1) is not 0 and len(l2) is not 0:
            if l1[0].y < l2[0].y:
                result.append(l1.pop(0))
            else:
                if l1[0].y > l2[0].y:
                    result.append(l2.pop(0))
                else: result.append(l1.pop(0) if l1[0].x < l2[0].x else l2.pop(0))

        #   return merge (either l1 or l2 is empty)
        return result + l1 + l2
    #   Print all values in a Vector2 list to the console
    @staticmethod
    def Print(VList):
        printList = ""
        for V in VList:
            printList += "(" + str(V.x) + "," + str(V.y) + ")"
        print(printList)


class Table:
    def __init__(self, id, vector2):
        self.id = id
        self.pos = vector2

def findClosestTable(lCurrent, lDesired):
    candidate = V2(float('inf'), float('inf'))
    for D in lDesired:
        for C in lCurrent:
            if D.Distance(C) < D.Distance(candidate):
                candidate = C
    return candidate

#   Current room state will be received in ID -> position pairs
currentTablePositions = [Table(0, V2(1,4)), Table(1, V2(4,3)), Table(2, V2(2,4))]
desiredTablePositions = [V2(4,1), V2(4,3), V2(4,4)]


'''
  Using Dijkstra based (A*) algorithm
  Reasons: Dealing with sudden stops of tables
  Finding the order of movement
  Swarm 
    



'''





