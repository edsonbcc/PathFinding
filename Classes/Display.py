class Display:
    #Constructor
    def __init__(self, size):
        self._size = size
        self._matrix = [[' ' for x in range(size)] for y in range(size)]

        #Construction of the format
        #I think this will change a bit...
        for x in range(0, size):
            self._matrix[0][x] = '_'
            self._matrix[size - 1][x] = '_'
            if x != 0:
                self._matrix[x][0] = '|'
            self._matrix[x][size - 1] = '|'

    #Don't know if this is usefull
    def getSize(self):
        return self._size

    def getPos(self, row, col):
        return self._matrix[row][col]

    def setPos(self, row, col, item):
        self._matrix[row][col] = item

    #Just show the display
    def showDisplay(self):
        for x in range(self._size):
            for y in range(self._size):
                print(self._matrix[x][y], end='')
            print()