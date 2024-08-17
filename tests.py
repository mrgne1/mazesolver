import unittest

from src.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1.cells),
                num_cols,
                )
        self.assertEqual(
                len(m1.cells[0]),
                num_rows,
                )

    def test_maze_cell_size(self):
        x = 10
        y = 11
        m1 = Maze(0, 0, 1, 1, x, y)
        width = m1.cells[0][0].x2 - m1.cells[0][0].x1
        self.assertEqual(width, x)
        height = m1.cells[0][0].y2 - m1.cells[0][0].y1
        self.assertEqual(height, y)

    def test_maze_cell_offset(self):
        x = 1
        y = 2
        m1 = Maze(x, y, 1, 1, 10, 10)
        self.assertEqual(m1.cells[0][0].x1, x)
        self.assertEqual(m1.cells[0][0].y1, y)

    def test_maze_cell_position(self):
        m1 = Maze(0, 0, 2, 2, 10, 10)
        self.assertEqual(m1.cells[0][0].x2, m1.cells[1][1].x1)
        self.assertEqual(m1.cells[0][0].y2, m1.cells[1][1].y1)

    def test_maze_entrance_and_exit(self):
        m1 = Maze(0, 0, 2, 2, 10, 10)
        self.assertFalse(m1.cells[0][0].has_top_wall)
        self.assertFalse(m1.cells[-1][-1].has_bottom_wall)

    def test_maze_reset_visited(self):
        m1 = Maze(0, 0, 2, 2, 10, 10)
        v1 = [cell.visited for col in m1.cells for cell in col]
        self.assertTrue(any(v1))
        m1._reset_cells_visited()
        v2 = [not cell.visited for col in m1.cells for cell in col]
        self.assertTrue(all(v2))


if __name__ == "__main__":
    unittest.main()
