import random
import time
from src.cell import Cell

class Maze(object):
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if seed is not None:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve_r(0, 0)

    def _create_cells(self):
        self.cells = []
        for i in range(self.num_cols):
            self.cells.append([])
            for j in range(self.num_rows):
                y1 = j * self.cell_size_y + self.y1 
                x1 = i * self.cell_size_x + self.x1
                y2 = y1 + self.cell_size_y
                x2 = x1 + self.cell_size_x
                self.cells[-1].append(Cell(x1, x2, y1, y2, window=self.win))
                
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self.cells[i][j]
        cell.draw()
        self._animate()

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
        cell = self.cells[i][j]
        cell.visited = True

        while True:
            to_visit = []
            if self._can_move(i-1, j):
                to_visit.append("left")
            if self._can_move(i, j-1):
                to_visit.append("up")
            if self._can_move(i+1, j):
                to_visit.append("right")
            if self._can_move(i, j+1):
                to_visit.append("down")
            if not to_visit:
                self._draw_cell(i, j)
                return
            direction = random.choice(to_visit)
            if direction == "left":
                cell.has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1, j)
            elif direction == "up":
                cell.has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j-1)
            elif direction == "right":
                cell.has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1, j)
            elif direction == "down":
                cell.has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False
                self._break_walls_r(i, j+1)

    def _reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False

    def _solve_r(self, i, j):
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        cell = self.cells[i][j]
        cell.visited = True
        for ii, jj, has_wall in [(i+1, j, cell.has_right_wall), (i, j+1, cell.has_bottom_wall), (i-1, j, cell.has_left_wall), (i, j-1, cell.has_top_wall)]:
            if not has_wall and self._can_move(ii, jj):
                cell.draw_move(self.cells[ii][jj])
                self._animate()
                if self._solve_r(ii, jj):
                    return True
                else:
                    cell.draw_move(self.cells[ii][jj], undo=True)
                    self._animate()

    def _can_move(self, i, j):
        col_inrange =  0 <= i < self.num_cols
        row_inrange =  0 <= j < self.num_rows
        return col_inrange and row_inrange and not self.cells[i][j].visited

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
        time.sleep(0.05)
