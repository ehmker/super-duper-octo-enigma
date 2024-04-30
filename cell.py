from graphics import Line, Point


class Cell:
    def __init__(self, win=None) -> None:
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.visited = False

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1=None, y1=None, x2=None, y2=None, linefill=None):
        if x1 is not None:
            self.set_cords(x1, y1, x2, y2)
        if linefill is None:
            linefill = "black"
        top_left_point = Point(self._x1, self._y1)
        top_right_point = Point(self._x2, self._y1)
        bot_left_point = Point(self._x1, self._y2)
        bot_right_point = Point(self._x2, self._y2)

        if self.has_top_wall:
            self._win.draw_line(Line(top_left_point, top_right_point), linefill)
        else:
            self._win.draw_line(Line(top_left_point, top_right_point), "#d9d9d9")

        if self.has_bottom_wall:
            self._win.draw_line(Line(bot_left_point, bot_right_point), linefill)
        else:
            self._win.draw_line(Line(bot_left_point, bot_right_point), "#d9d9d9")

        if self.has_left_wall:
            self._win.draw_line(Line(top_left_point, bot_left_point), linefill)
        else:
            self._win.draw_line(Line(top_left_point, bot_left_point), "#d9d9d9")

        if self.has_right_wall:
            self._win.draw_line(Line(top_right_point, bot_right_point), linefill)
        else:
            self._win.draw_line(Line(top_right_point, bot_right_point), "#d9d9d9")

    def set_cords(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"

        from_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_center = Point(
            (to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2
        )
        self._win.draw_line(Line(from_center, to_center), color)
