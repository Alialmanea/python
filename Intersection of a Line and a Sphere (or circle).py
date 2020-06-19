from math import sqrt

class Point():
    def __init__(self, X ,Y):
        self.__X = X
        self.__Y = Y

    def __str__(self):
        return "({}, {})".format(self.getX(), self.getY())

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def print(self):
        print("({}, {})".format(self.__X,self.__Y))

class Line():
    def __init__(self, P1, P2):
        self.__P1 = P1
        self.__P2 = P2

    def getPoint1(self):
        return self.__P1

    def getpoint2(self):
        return self.__P2

    def __str__(self):
        return '{}--------{}'.format(self.__P1, self.__P2)


class Circle:
    def __init__(self, Center, Radius):
        self.__Center = Center
        self.__Radius = Radius
        print(type(self.__Center))
    def __str__(self):
        return ' Center of Circle : {}   Radius : {}'.format(self.__Center,self.__Radius)
    def getCenter(self):
        return self.__Center
    def getRadius(self):
        return self.__Radius

def sphere_line_intersection(line, circle):
    def square(f):
        return f * f

    X1 = line.getPoint1().getX()
    X2 = line.getpoint2().getX()
    X3 = circle.getCenter().getX()
    Y1 = line.getPoint1().getY()
    Y2 = line.getpoint2().getY()
    Y3 = circle.getCenter().getY()
    r = circle.getRadius()

    a = square(X2 - X1) + square(Y2 - Y1)

    b = 2.0 * ((X2 - X1) * (X1 - X3) +
               (Y2 - Y1) * (Y1 - Y3))

    c = (square(X3) + square(Y3) + square(X1) +
         square(Y1) - 2.0 * (X3 * X1 + Y3 * Y1) - square(r))

    #print(a,b,c)

    p1 = p2 = None

    i = b * b - 4.0 * a * c

    if i < 0.0:
        pass
    elif i == 0.0:
        # one intersection
        mu = -b / (2.0 * a)
        p1 = (X1 + mu * (X2 - X1),
              Y1 + mu * (Y2 - Y1))


    elif i > 0.0:
        # first intersection
        mu = (-b + sqrt(i)) / (2.0 * a)
        p1 = (X1 + mu * (X2 - X1),
              Y1 + mu * (Y2 - Y1))

        # second intersection
        mu = (-b - sqrt(i)) / (2.0 * a)
        p2 = (X1 + mu * (X2 - X1),
              Y1 + mu * (Y2 - Y1))

    return Point(p1, p2)



def main():
    circle = Circle(Point(4, 3), 2)
    line1 = Line(Point(-2, -2), Point(1, 1))
    print(sphere_line_intersection(line1, circle))

    line2 = Line(Point(1, 3), Point(0, 0))
    print(sphere_line_intersection(line2, circle))

    line3 = Line(Point(6, 5), Point(6, 1))
    print(sphere_line_intersection(line3, circle))


main()
