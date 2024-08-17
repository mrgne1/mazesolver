from src.line import Line
from src.point import Point

class Cell(object):
    def __init__(self,x1, x2, y1, y2, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True, window=None):
        self.win = window
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.clear = "#d9d9d9"
        self.visited = False

    def draw(self, fill_color="black"):
        if self.win is None:
            return

        color = self.clear
        if self.has_left_wall:
            color = fill_color
        p1 = Point(self.x1, self.y1)
        p2 = Point(self.x1, self.y2)
        l = Line(p1, p2)
        l.draw(self.win.canvas, fill_color=color)

        color = self.clear
        if self.has_right_wall:
            color = fill_color
        p1 = Point(self.x2, self.y1)
        p2 = Point(self.x2, self.y2)
        l = Line(p1, p2)
        l.draw(self.win.canvas, fill_color=color)

        color = self.clear
        if self.has_top_wall:
            color = fill_color
        p1 = Point(self.x1, self.y1)
        p2 = Point(self.x2, self.y1)
        l = Line(p1, p2)
        l.draw(self.win.canvas, fill_color=color)

        color = self.clear
        if self.has_bottom_wall:
            color = fill_color
        p1 = Point(self.x1, self.y2)
        p2 = Point(self.x2, self.y2)
        l = Line(p1, p2)
        l.draw(self.win.canvas, fill_color=color)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        bx = (self.x1 + self.x2) / 2
        by = (self.y1 + self.y2) / 2
        ex = (to_cell.x1 + to_cell.x2) / 2
        ey = (to_cell.y1 + to_cell.y2) / 2
        move = Line(Point(bx, by), Point(ex, ey))
        if self.win is not None:
            move.draw(self.win.canvas, fill_color=color)

