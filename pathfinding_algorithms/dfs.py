from time import sleep
from collections import deque

from pathfinding_algorithms.pathfinder import PassFinder
from grid.grid import Grid
from settings.settings import *


class DfsSearch(PassFinder):
    def __init__(self, grid: Grid):
        self.__grid = grid
        self.__routes = [[None] * self.__grid.height for _ in range(self.__grid.width)]
        self.__visited = [[False] * self.__grid.height for _ in range(self.__grid.width)]
        self.found_path = False

    def solve(self, canvas):
        self.__find_path(self.__grid.start_cell, canvas)
        if self.found_path:
            self.__get_path(self.__grid.dest_cell, canvas)

    def __get_path(self, start, canvas):
        curr = start
        while self.__routes[curr.x][curr.y]:
            canvas.update()
            sleep(0.01)
            self.__grid.set_color(curr, CELL_COLOR['route'], canvas)
            curr = self.__routes[curr.x][curr.y]

    def __find_path(self, start, canvas):
        q = deque()
        q.append(start)
        self.__visited[start.x][start.y] = True
        while len(q) != 0:
            curr = q.pop()
            if curr == self.__grid.dest_cell:
                self.found_path = True
                return
            canvas.update()
            sleep(0.01)
            self.__grid.set_color(curr, CELL_COLOR['visited'], canvas)
            for c in curr.neighbours():
                if  not self.__grid.is_obstacle(c) and not self.__visited[c.x][c.y]:
                    self.__visited[c.x][c.y] = True
                    q.append(c)
                    self.__routes[c.x][c.y] = curr

