from graphics import Window, Point, Line
from cell import Cell
from maze import Maze
import random


def ran_lines(num):
    line_list = []
    for i in range(num):
        points = random.sample(range(500), 4)
        A = Point(points[0], points[1])
        B = Point(points[2], points[3])
        line_list.append(Line(A, B))
    return line_list


def ran_cells(num, win):
    def ran_walls(c):
        wall_probability = 0.2
        if random.random() < wall_probability:
            c.has_top_wall = False
        if random.random() < wall_probability:
            c.has_bot_wall = False
        if random.random() < wall_probability:
            c.has_left_wall = False
        if random.random() < wall_probability:
            c.has_right_wall = False
        return

    cell_list = []
    for i in range(num):
        point = random.sample(range(400), 2)
        c = Cell(win)
        ran_walls(c)
        c.draw(point[0], point[1], point[0] - 25, point[1] + 25)
        cell_list.append(c)
    return cell_list


def other():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)

    win.wait_for_close()


def main():
    my_window = Window(750, 750)
    # lines = ran_lines(5)
    # for l in lines:
    #     my_window.draw_line(l, "green")

    # cells = ran_cells(10, my_window)
    # for i in range(len(cells) - 1):
    #     cells[i].draw_move(cells[i + 1])
    num_cols = 12
    num_rows = 10
    # m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    m = Maze(10, 10, num_rows, num_cols, 50, 50, my_window, 10)
    m.solve()
    my_window.wait_for_close()


main()
