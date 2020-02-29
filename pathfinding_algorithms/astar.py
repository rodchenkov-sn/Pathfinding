from time import sleep
from queue import PriorityQueue
from math import sqrt, pow

from pathfinding_algorithms.pathfinder import PassFinder
from grid.grid import Grid
from settings.settings import *


class AStar(PassFinder):
    def __init__(self, grid: Grid):
        super().__init__(grid)

    def solve(self, canvas):
        self.__find_path(self.grid.start_cell, canvas)
        if self.found_path:
            self.get_path(self.grid.dest_cell, canvas)

    def __find_path(self, start, canvas):
        q = PriorityQueue()
        q.put((0, start))
        self.visited[start.x][start.y] = True
        while not q.empty():
            _, curr = q.get()
            if curr == self.grid.dest_cell:
                self.found_path = True
                return
            canvas.update()
            sleep(0.01)
            self.grid.set_color(curr, CELL_COLOR['visited'], canvas)
            for c in curr.neighbours():
                if not self.grid.is_obstacle(c) and not self.visited[c.x][c.y]:
                    self.visited[c.x][c.y] = True
                    q.put((self.__compute_priority(c), c))
                    self.routes[c.x][c.y] = curr

    def __compute_priority(self, cell):
        sx = self.grid.start_cell.x
        sy = self.grid.start_cell.y
        cx = cell.x
        cy = cell.y
        dx = self.grid.dest_cell.x
        dy = self.grid.dest_cell.y
        from_start = sqrt(pow(sx - cx, 2) + pow(sy - cy, 2))
        to_dest = sqrt(pow(dx - cx, 2) + pow(dy - cy, 2))
        return from_start + to_dest
