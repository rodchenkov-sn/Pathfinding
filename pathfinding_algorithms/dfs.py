from time import sleep

from grid.grid import Grid


class DfsSearch:
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
            self.__grid.set_color(curr, '#1dcc25', canvas)
            curr = self.__routes[curr.x][curr.y]

    def __find_path(self, start, canvas):
        prev = None
        stack = [start]
        while len(stack) != 0:
            curr = stack.pop(len(stack) - 1)
            if not self.__visited[curr.x][curr.y]:
                self.__visited[curr.x][curr.y] = True
                canvas.update()
                sleep(0.01)
                self.__grid.set_color(curr, '#ffde4a', canvas)
                self.__routes[curr.x][curr.y] = prev
                if curr == self.__grid.dest_cell:
                    self.found_path = True
                    return
                prev = curr
                for c in curr.neighbours():
                    if c.x < self.__grid.width and c.y < self.__grid.height and not self.__grid.is_obstacle(c):
                        stack.append(c)
