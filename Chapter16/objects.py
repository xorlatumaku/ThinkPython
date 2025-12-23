# Date: 06/12/2025
# Program to implement object-oriented programming

class Point:
    """ Represent a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def translated(self, dx=0, dy=0):
        point = copy(self)
        point.translate(dx, dy)
        return point

start = Point(0, 0)
print(start)

from copy import copy
end1 = copy(start)
end1.translate(300, 0)
print(end1)

end2 = start.translated(0, 150)
print(end2)

# Creating a Line
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'

    def draw(self):
        jumpto(self.p1.x, self.p1.y)
        moveto(self.p2.x, self.p2.y)

line1 = Line(start, end1)
print(line1)


from jupyturtle import make_turtle, jumpto, moveto
line2 = Line(start, end2)
print(line2)

make_turtle()
line1.draw()
line2.draw()
