from time import sleep

from grid.grid import Grid
from settings.settings import *


class PassFinder:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.routes = [[None] * self.grid.height for _ in range(self.grid.width)]
        self.visited = [[False] * self.grid.height for _ in range(self.grid.width)]
        self.found_path = False

    def solve(self, canvas):
        pass

    def get_path(self, start, canvas):
        curr = start
        while self.routes[curr.x][curr.y]:
            canvas.update()
            sleep(DELAY_TIME)
            self.grid.set_color(curr, CELL_COLOR['route'], canvas)
            curr = self.routes[curr.x][curr.y]
