from time import sleep
from queue import PriorityQueue
from math import sqrt, pow

from pathfinding_algorithms.pathfinder import PassFinder
from grid.grid import Grid
from settings.settings import *


class AStar(PassFinder):
    def __init__(self, grid: Grid):
        self.__grid = grid
        self.__routes = [[None] * self.__grid.height for _ in range(self.__grid.width)]
        self.__visited = [[False] * self.__grid.height for _ in range(self.__grid.width)]
        self.found_path = False

    def solve(self, canvas):
        self.__find_path(self.__grid.start_cell, canvas)
        if self.found_path:
            self.__get_path(self.__grid.dest_cell, canvas)

    def __find_path(self, start, canvas):
        q = PriorityQueue()
        q.put((0, start))
        self.__visited[start.x][start.y] = True
        while not q.empty():
            _, curr = q.get()
            if curr == self.__grid.dest_cell:
                self.found_path = True
                return
            canvas.update()
            sleep(0.01)
            self.__grid.set_color(curr, CELL_COLOR['visited'], canvas)
            for c in curr.neighbours():
                if not self.__grid.is_obstacle(c) and not self.__visited[c.x][c.y]:
                    self.__visited[c.x][c.y] = True
                    q.put((self.__compute_priority(c), c))
                    self.__routes[c.x][c.y] = curr

    def __compute_priority(self, cell):
        sx = self.__grid.start_cell.x
        sy = self.__grid.start_cell.y
        cx = cell.x
        cy = cell.y
        dx = self.__grid.dest_cell.x
        dy = self.__grid.dest_cell.y
        from_start = sqrt(pow(sx - cx, 2) + pow(sy - cy, 2))
        to_dest = sqrt(pow(dx - cx, 2) + pow(dy - cy, 2))
        return from_start + to_dest

    def __get_path(self, start, canvas):
        curr = start
        while self.__routes[curr.x][curr.y]:
            canvas.update()
            sleep(0.01)
            self.__grid.set_color(curr, CELL_COLOR['route'], canvas)
            curr = self.__routes[curr.x][curr.y]
