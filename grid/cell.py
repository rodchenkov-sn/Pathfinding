class Cell:
    def __init__(self, x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError('Expected positive or zero numbers at Cell.__init__')
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def neighbours(self):
        nbs = []
        if self.x > 0:
            nbs.append(Cell(self.x - 1, self.y))
        if self.y > 0:
            nbs.append(Cell(self.x, self.y - 1))
        nbs.append(Cell(self.x + 1, self.y))
        nbs.append(Cell(self.x, self.y + 1))
        return nbs
