from src.window import Window
from src.cell import Cell

if __name__ == "__main__":
    win = Window(100, 100)
    cells = []
    for x in range(0, 100, 25):
        for y in range(0, 100, 25):
            cells.append(Cell(win, x1=x+4, x2=x + 25, y1=y+4, y2=y + 25, has_right_wall=False, has_left_wall=False))
    for cell in cells:
        cell.draw()

    a, b = cells[:2]
    a.draw_move(b, undo=True)

    win.wait_for_close()


