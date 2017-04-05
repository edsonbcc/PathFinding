from math import sqrt
from Classes import Display

#I don't wanted to use this class outside the scope of the Agent. That's why creating an agent takes so many parameters!
class Position:
    def __init__(self, row, col):
        self._posX = row
        self._posY = col

    def getRow(self):
        return self._posX

    def getCol(self):
        return self._posY

    def getCost(self):
        return self._cost

    def getParent(self):
        return self._parent

    def setCost(self, value):
        self._cost = value

    def setParent(self, parent):
        self._parent = parent

class Sensor:
    def __init__(self, display):
        self._display = display

    def getSuccessors(self, row, col):
        successors = []
        size = self._display.getSize()

        #This is going to be horrible
        if row < size:
            successors.append(Position(row + 1, col))
        if row < size and col < size:
           successors.append(Position(row + 1, col + 1))
        if col < size:
            successors.append(Position(row, col + 1))
        if row >= 0:
            successors.append(Position(row - 1, col))
        if col >= 0:
            successors.append(Position(row, col - 1))
        if row >= 0 and col >= 0:
            successors.append(Position(row - 1, col - 1))
        if col >= 0 and row < size:
            successors.append(Position(row + 1, col - 1))
        if row >= 0 and col < size:
            successors.append(Position(row - 1, col + 1))
        return successors

    def getCost(self, pos):
        return self._display.getPos(pos.getRow(), pos.getCol())

    def getHeuristics(self, pos, dest):
        posX = pos.getRow()
        posY = pos.getCol()
        destX = dest.getRow()
        destY = dest.getCol()

        if posX - destX == 0:
            return posY - destY
        elif posY - destY == 0:
            return posX - destX
        else:
            return sqrt(abs(posX - destX)**2 + abs(posY - destY)**2)

class Atuator:
    def __init__(self, display):
        self._display = display

    def setDisPos(self, pos):
        self._display.setPos(pos.getRow(), pos.getCol(), -1) # -1 is the path

class Agent:
    #I think the agent need to know the display. This looks like a gambiarra, but i don't know what else to do. If you know, do as you wish.
    def __init__(self, origX, origY, destX, destY, display):
        self._sens = Sensor(display)
        self._pos = Position(origX, origY, 0)
        self._dest = Position(destX, destY, 0)
        self._att = Atuator(display)

    def _nodeWithLeastF(self, openList):
        q = 0
        leastCost = openList[q].getCost()

        for i in range(1, len(openList)):
            actualCost = openList[i].getCost()
            if leastCost > actualCost:
                leastCost = actualCost
                q = i
        return q

    def _setParent(self, suc, parent):
        suc.setParent(parent)

    def _betterPosition(self, positions, pos):
        for position in positions:
            if pos.getRow() == position.getRow() and pos.getCol() == position.getCol() and pos.getCost() > position.getCost():
                return True
        return False

    #Gets the path and return use it
    def _pathFinding(self, pos):
        actual = pos
        while actual is not None:
            self._pathFinding(actual)
            actual = actual.getParent()

    """
    The Only Function that needs to be used.
        If True = A path exist
        If False = Don't exist
    """
    def aStar(self):
        openList = []
        closedList = []

        self._pos.setCost(0)
        openList.append(self._pos)

        while len(openList) != 0:
            q = openList.pop(self._nodeWithLeastF(openList))
            successors = self._sens.getSuccessors(q.getRow(), q.getCol())

            for suc in successors:
                if suc == self._dest:
                    self._pathFinding(suc)
                    return True

                successorG = self._sens.getCost(suc) + 1
                successorH = self._sens.getHeuristics(suc, self._dest)
                successorF = successorG + successorH
                suc.setCost(successorF)

                if not (self._betterPosition(openList, suc)) and (not self._betterPosition(closedList, suc)):
                    self._setParent(suc, q)
                    openList.append(suc)

            closedList.append(q)

        return False