from time import sleep
from collections import deque

from pathfinding_algorithms.pathfinder import PassFinder
from grid.grid import Grid
from settings.settings import *


class DfsSearch(PassFinder):
    def __init__(self, grid: Grid):
        super().__init__(grid)

    def solve(self, canvas):
        self.__find_path(self.grid.start_cell, canvas)
        if self.found_path:
            self.get_path(self.grid.dest_cell, canvas)

    def __find_path(self, start, canvas):
        q = deque()
        q.append(start)
        self.visited[start.x][start.y] = True
        while len(q) != 0:
            curr = q.pop()
            if curr == self.grid.dest_cell:
                self.found_path = True
                return
            canvas.update()
            sleep(0.01)
            self.grid.set_color(curr, CELL_COLOR['visited'], canvas)
            for c in curr.neighbours():
                if not self.grid.is_obstacle(c) and not self.visited[c.x][c.y]:
                    self.visited[c.x][c.y] = True
                    q.append(c)
                    self.routes[c.x][c.y] = curr

