from src.window import Window
from src.cell import Cell
from src.maze import Maze

if __name__ == "__main__":
    win = Window(200, 200)
    maze = Maze(3, 3, 10, 15, 25, 25, win)

    win.wait_for_close()


