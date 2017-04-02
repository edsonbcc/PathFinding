from random import randint

class Position:
    def __init__(self, row, col, value):
        self._posX = row
        self._posY = col

        #Don't know if this is a good ideia
        if value == '#':
            self._cost = 99999999
        else:
            self._cost = randint(0, 50)

    def getCost(self):
        return self._cost

class Agent:
    #I think the agent need to know the display. This looks like a gambiarra, but i don't know what else to do. If you know, do as you wish.
    def __init__(self, orig, display):
        self._pos = orig
        self._display = display

    def _nodeWithLeastF(self, openList):
        q = 0
        leastCost = openList[q].getCost()

        for i in range(1, len(openList)):
            actualCost = openList[i].getCost()
            if leastCost > actualCost:
                leastCost = actualCost
                q = i
        return q


    def aStar(self):
        openList = [self._pos]
        closedList = []

        while len(openList) != 0:
            q = openList.pop(self._nodeWithLeastF(openList))
