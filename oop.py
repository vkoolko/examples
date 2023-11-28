from math import sqrt


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.segments = []
        self.segments.append(LineTo(0, 0))
        self.segments += [segment for segment in args]

    def get_path(self):
        return self.segments

    def get_length(self):
        l = 0
        values = [tuple(self.segments[i:i+2]) for i in range(len(self.segments)-1)]
        for first, second in values:
            l += sqrt((second.x - first.x) ** 2 + (second.y - first.y) ** 2)
        return l

    def add_line(self, line):
        self.segments.append(line)


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)
