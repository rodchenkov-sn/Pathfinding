import tkinter as tk

from grid.grid import Grid
from pathfinding_algorithms import dfs, bfs
from window.window_stage import WindowStage


class MainWindow:
    def __init__(self, width: int, height: int):
        if width <= 0 or height <= 0:
            raise ValueError('Expected positive width and height at MainWindow.__init__')
        self.__stage = WindowStage.EDIT_OBSTACLES
        self.__width = width
        self.__height = height
        self.__grid = Grid(50, 50)
        self.__root = tk.Tk()
        self.__canvas = tk.Canvas(self.__root, width=self.__width, height=self.__height, bg='white')
        self.__canvas.pack(padx=10, pady=10)
        self.__canvas.bind('<Button-1>', self.__on_canvas_click)
        self.__algorithm = tk.StringVar()
        self.__algorithm.set('DFS')
        tk.Button(
            self.__root, text='obstacle', bg='black', fg='white',
            command=lambda _=None: self.__set_stage(WindowStage.EDIT_OBSTACLES)
        ).pack(padx=10, pady=5, side=tk.LEFT)
        tk.Button(
            self.__root, text='start', bg='cyan',
            command=lambda _=None: self.__set_stage(WindowStage.EDIT_START)
        ).pack(padx=10, pady=5, side=tk.LEFT)
        tk.Button(
            self.__root, text='destination', bg='blue', fg='white',
            command=lambda _=None: self.__set_stage(WindowStage.EDIT_DESTINATION)
        ).pack(padx=10, pady=5, side=tk.LEFT)
        tk.Button(
            self.__root, text='solve', bg='green', fg='white',
            command=lambda _=None: self.__solve()
        ).pack(padx=10, pady=5, side=tk.LEFT)
        tk.OptionMenu(
            self.__root, self.__algorithm, 'DFS', 'BFS', 'A*'
        ).pack(padx=10, pady=5, side=tk.LEFT)
        self.__solvers = {
            'DFS': dfs.DfsSearch,
            'BFS': bfs.BfsSearch
        }

    def main_loop(self):
        self.__grid.draw(self.__canvas)
        self.__root.mainloop()

    def __solve(self):
        if self.__grid.start_cell and self.__grid.dest_cell:
            prev_stage = self.__stage
            self.__stage = WindowStage.FINDING_PATH
            self.__grid.reset_colors()
            self.__grid.draw(self.__canvas)
            solve_way = self.__algorithm.get()
            if solve_way in self.__solvers:
                self.__solvers[solve_way](self.__grid).solve(self.__canvas)  # word 'solve' occurred three times!
            else:
                raise NotImplementedError('WIP')
            self.__stage = prev_stage

    def __set_stage(self, stage):
        if self.__stage != WindowStage.FINDING_PATH:
            self.__stage = stage

    def __on_canvas_click(self, event):
        if self.__stage == WindowStage.FINDING_PATH:
            return
        self.__grid.reset_colors()
        cell_clicked = self.__grid.get_cell_by_coord(self.__width, self.__height, event.x, event.y)
        if self.__stage == WindowStage.EDIT_OBSTACLES:
            if self.__grid.is_obstacle(cell_clicked):
                self.__grid.unset_obstacle(cell_clicked)
            elif self.__grid.is_free(cell_clicked):
                self.__grid.set_obstacle(cell_clicked)
        elif self.__stage == WindowStage.EDIT_START and self.__grid.is_free(cell_clicked):
            self.__grid.start_cell = cell_clicked
        elif self.__stage == WindowStage.EDIT_DESTINATION and self.__grid.is_free(cell_clicked):
            self.__grid.dest_cell = cell_clicked
        self.__grid.draw(self.__canvas)
