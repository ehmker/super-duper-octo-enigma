from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, w, h) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver Window")

        self.__canvas = Canvas(width=w, height=h)
        self.__canvas.pack()

        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
        pass


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self.p1 = a
        self.p2 = b

    def draw(self, c: Canvas, fill_color) -> None:
        c.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2,
        )
