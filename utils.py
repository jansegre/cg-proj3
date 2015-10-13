from PIL import Image


class Window(object):

    def __init__(self, width, height, (x0, x1), (y0, y1)):
        self.width = width
        self.height = height
        self._0 = tuple(map(float, (x0, y0)))
        self._1 = tuple(map(float, (x1, y1)))
        self.image = Image.new('1', self.size)
        self.pix = self.image.load()

    @property
    def size(self):
        return (self.width, self.height)

    def pixels(self):
        for px in range(self.width):
            for py in range(self.height):
                yield px, py

    def in_screen(self, px, py):
        return 0 <= px < self.width and 0 <= py < self.height

    def to_screen(self, x, y):
        (x0, y0), (x1, y1) = self._0, self._1
        px = int(round((x - x0) / (x1 - x0) * self.width))
        py = int(round((y - y1) / (y0 - y1) * self.height))
        return px, py

    def from_screen(self, px, py):
        (x0, y0), (x1, y1) = self._0, self._1
        x = x0 + (x1 - x0) * float(px) / self.width
        y = y1 + (y0 - y1) * float(py) / self.height
        return x, y
