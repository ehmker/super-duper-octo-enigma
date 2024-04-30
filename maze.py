from cell import Cell
import time
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.__win = win

        if seed:
            random.seed(seed)

        self._cells = self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        # self._cells[0][3].draw(linefill="blue")

    def _create_cells(self):
        cell_matrix = []
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                c = self._draw_cell(i, j)

                row.append(c)
            cell_matrix.append(row)

        return cell_matrix

    def _draw_cell(self, i, j):
        x1 = self._x1 + self._cell_size_x * i
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + self._cell_size_y * j
        y2 = y1 + self._cell_size_y
        if self.__win is not None:
            c = Cell(self.__win)
            c.draw(x1, y1, x2, y2)
            self._animate()

        return c

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        # print(f"visiting {i}, {j}")
        while True:
            valid_movements = self._valid_moves(i, j)

            # print(valid_movements)
            if valid_movements == []:
                self._cells[i][j].draw()
                # self._draw_cell(i, j)
                # print("drawing")
                return

            direction = random.choice(valid_movements)
            # print(direction)
            if direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j].draw()
                self._cells[i][j - 1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)
            elif direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j].draw()
                self._cells[i][j + 1].has_top_wall = False
                self._break_walls_r(i, j + 1)
            elif direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i][j].draw()
                self._cells[i - 1][j].has_right_wall = False
                self._break_walls_r(i - 1, j)
            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i][j].draw()
                self._cells[i + 1][j].has_left_wall = False
                self._break_walls_r(i + 1, j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for cell in self._cells[i]:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        valid_movement = self._valid_moves(i, j)
        for direction in valid_movement:
            if (
                direction == "up"
                and not self._cells[i][j].has_top_wall
                and not self._cells[i][j - 1].has_bottom_wall
            ):
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
            if (
                direction == "down"
                and not self._cells[i][j].has_bottom_wall
                and not self._cells[i][j + 1].has_top_wall
            ):
                self._cells[i][j].draw_move(self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)

            if (
                direction == "left"
                and not self._cells[i][j].has_left_wall
                and not self._cells[i - 1][j].has_right_wall
            ):
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)

            if (
                direction == "right"
                and not self._cells[i][j].has_right_wall
                and not self._cells[i + 1][j].has_left_wall
            ):
                self._cells[i][j].draw_move(self._cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)

        return False

    def _valid_moves(self, i, j):
        directions = []
        if j - 1 >= 0 and not self._cells[i][j - 1].visited:
            directions.append("up")
        if j + 1 < self._num_rows and not self._cells[i][j + 1].visited:
            directions.append("down")
        if i - 1 >= 0 and not self._cells[i - 1][j].visited:
            directions.append("left")
        if i + 1 < self._num_cols and not self._cells[i + 1][j].visited:
            directions.append("right")

        return directions
