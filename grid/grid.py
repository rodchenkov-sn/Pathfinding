from grid.cell import Cell
from settings.settings import *


class Grid:
    def __init__(self, height: int, width: int):
        if height < 1 or width < 1:
            raise ValueError('Expected positive height and width at Grid.__init__')
        self.height = height
        self.width = width
        self.__obstacles = self.__start_cell = self.__dest_cell = self.__color_scheme = None
        self.reset()

    def draw(self, canvas):
        canvas.update()
        canvas.delete('all')
        cell_width = canvas.winfo_width() // self.width
        cell_height = canvas.winfo_height() // self.height
        for i in range(self.width):
            for j in range(self.height):
                if self.__obstacles[i][j]:
                    fill_color = CELL_COLOR['obstacle']
                elif self.start_cell and self.start_cell == Cell(i, j):
                    fill_color = CELL_COLOR['start']
                elif self.dest_cell and self.dest_cell == Cell(i, j):
                    fill_color = CELL_COLOR['destination']
                elif self.__color_scheme[i][j]:
                    fill_color = self.__color_scheme[i][j]
                else:
                    fill_color = CELL_COLOR['free']
                canvas.create_rectangle(i * cell_width, j * cell_height,
                                        (i + 1) * cell_width, (j + 1) * cell_height, fill=fill_color)

    def get_cell_by_coord(self, width: int, height: int, x: int, y: int):
        if x > width or y > height:
            return None
        cell_width = width // self.width
        cell_height = height // self.height
        return Cell(x // cell_width, y // cell_height)

    def set_obstacle(self, position: Cell):
        if position.x >= self.width or position.y >= self.height:
            raise IndexError('Position was out of grid at Grid.set_obstacle')
        self.__obstacles[position.x][position.y] = True

    def unset_obstacle(self, position: Cell):
        if position.x >= self.width or position.y >= self.height:
            raise IndexError('Position was out of grid at Grid.unset_obstacle')
        self.__obstacles[position.x][position.y] = False

    def is_obstacle(self, position: Cell):
        if position.x >= self.width or position.y >= self.height:
            return True
        return self.__obstacles[position.x][position.y]

    def set_color(self, position: Cell, color: str, canvas=None):
        if position.x >= self.width or position.y >= self.height:
            raise IndexError('Position was out of grid at Grid.set_color')
        if position != self.start_cell and position != self.dest_cell:
            self.__color_scheme[position.x][position.y] = color
            if canvas and position not in [self.__start_cell, self.__dest_cell]:
                cell_width = canvas.winfo_width() // self.width
                cell_height = canvas.winfo_height() // self.height
                canvas.create_rectangle(
                    position.x * cell_width, position.y * cell_height,
                    (position.x + 1) * cell_width, (position.y + 1) * cell_height, fill=color
                )

    def reset_colors(self):
        self.__color_scheme = [[None] * self.height for i in range(self.width)]

    def get_color(self, position: Cell):
        if position.x >= self.width or position.y >= self.height:
            raise IndexError('Position was out of grid at Grid.get_color')
        return self.__color_scheme[position.x][position.y]

    def is_free(self, position: Cell):
        if position.x >= self.width or position.y >= self.height:
            raise IndexError('Position was out of grid at Grid.is_free')
        return not self.is_obstacle(position) and (not self.start_cell or self.start_cell != position) \
               and (not self.dest_cell or self.dest_cell != position)

    @property
    def start_cell(self):
        return self.__start_cell

    @property
    def dest_cell(self):
        return self.__dest_cell

    @start_cell.setter
    def start_cell(self, position: Cell):
        if position.x >= self.width or position.y >= self.height:
            raise IndexError('Position was out of grid at Grid.start_cell.setter')
        if self.__obstacles[position.x][position.y]:
            raise IndexError('Expected start point on free space at Grid.start_cell.setter')
        self.__start_cell = position

    @dest_cell.setter
    def dest_cell(self, position: Cell):
        if position.x >= self.width or position.y >= self.height:
            raise IndexError('Position was out of grid at Grid.dest_cell.setter')
        if self.__obstacles[position.x][position.y]:
            raise IndexError('Expected start point on free space at Grid.dest_cell.setter')
        self.__dest_cell = position

    def reset(self):
        self.__obstacles = [[0] * self.height for i in range(self.width)]
        self.__start_cell = None
        self.__dest_cell = None
        self.__color_scheme = [[None] * self.height for i in range(self.width)]
