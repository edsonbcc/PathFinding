from math import sqrt

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

    def setCost(self, value):
        self._cost = value

    def setParent(self, parent):
        self._parent = parent

class Sensor:
    def __init__(self, display):
        self._display = display

    def getSuccessors(self, row, col):
        successors = []

        successors.append(Position(row + 1, col))
        successors.append(Position(row + 1, col + 1))
        successors.append(Position(row, col + 1))
        successors.append(Position(row - 1, col))
        successors.append(Position(row, col - 1))
        successors.append(Position(row - 1, col - 1))
        successors.append(Position(row + 1, col - 1))
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

class Agent:
    #I think the agent need to know the display. This looks like a gambiarra, but i don't know what else to do. If you know, do as you wish.
    def __init__(self, origX, origY, destX, destY, display):
        self._sens = Sensor(display)
        self._pos = Position(origX, origY, 0)
        self._dest = Position(destX, destY, 0)

    def _nodeWithLeastF(self, openList):
        q = 0
        leastCost = openList[q].getCost()

        for i in range(1, len(openList)):
            actualCost = openList[i].getCost()
            if leastCost > actualCost:
                leastCost = actualCost
                q = i
        return q

    def _setParent(self, sucessors, parent):
        for suc in sucessors:
            suc.setParent(parent)

    def _betterPosition(self, positions, pos):
        """
        Needs to be done. It's a function that see if there is any better option than "pos".
        Returns True if exist a better Position
        and
        Returns False if not
        """""

    #Needs to be completed and needs to be tested.
    def aStar(self):
        openList = []
        closedList = []

        self._pos.setCost(0)
        openList.append(self._pos)

        while len(openList) != 0:
            q = openList.pop(self._nodeWithLeastF(openList))
            successors = self._sens.getSuccessors(q.getRow(), q.getCol())
            self._setParent(successors, q)

            for suc in successors:
                if suc == self._dest:
                    return #Here needs to be implemented a function that returns the path to the destiny
                successorG = self._sens.getCost(suc) + 1
                successorH = self._sens.getHeuristics(suc, self._dest)
                successorF = successorG + successorH
                suc.setCost(successorF)

                if not (_betterPosition(openList, suc)) and (not _betterPosition(closedList, suc)):
                    openList.append(suc)

            closedList.append(q)