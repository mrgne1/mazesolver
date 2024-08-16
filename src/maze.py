import time
from src.cell import Cell

class Maze(object):
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()
        
    def _create_cells(self):
        self.cells = [[Cell(self.win, 1, 1, 1, 1) for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self.cells[i][j]
        cell.x1 = i * self.cell_size_x + self.x1 
        cell.y1 = j * self.cell_size_y + self.y1
        cell.x2 = cell.x1 + self.cell_size_x
        cell.y2 = cell.y1 + self.cell_size_y
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
