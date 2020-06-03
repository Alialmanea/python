import math

class P:   # To Make a Specific Point
    def __init__(self,X,Y): # Construction of Point class
        self.X=X
        self.Y=Y
    def print(self):  # Print the Point (X, Y)
        print("({},{})".format(self.X,self.Y))

class Line: # To Make Line by Using two specific points
    def __init__(self,p1,p2): # Construction of Line class
        self.p1=p1
        self.p2=p2
    def print(self):
        print("({},{}) ______________ ({},{})".format(self.p1.X,self.p1.Y,self.p2.X,self.p2.Y))


class Circle: # To Make Circle by Using 3 points
    def __init__(slef,P1,P2,P3):
        slef.Radius=-1    #Error checking
        slef.P1=P1
        slef.P2=P2
        slef.P3=P3
        slef.Center=P(-1, -1) #Error checking

        """If either Line is vertical then the corresponding slope is infinite.
        Can be solved by simply rearranging the order of the points so that vertical lines do not occur. """

        if not slef.__IsPerpendicular(slef.P1,slef.P2,slef.P3):
            slef.__CalcCircle(slef.P1,slef.P2,slef.P3)
        if not slef.__IsPerpendicular(slef.P1,slef.P3,slef.P2):
            slef.__CalcCircle(slef.P1,slef.P3,slef.P2)
        if not slef.__IsPerpendicular(slef.P2,slef.P1,slef.P3):
            slef.__CalcCircle(slef.P2,slef.P1,slef.P3)
        if not slef.__IsPerpendicular(slef.P3,slef.P2,slef.P1):
            slef.__CalcCircle(slef.P3,slef.P2,slef.P1)
        if not slef.__IsPerpendicular(slef.P3,slef.P1,slef.P2):
            slef.__CalcCircle(slef.P3,slef.P1,slef.P2)
        else: # The three Point are perpendicular to axis
            slef.Radius=-1
            slef.Center=P(-1, -1)

    # private function
    def __IsPerpendicular(self,P1,P2,P3): # Check the given point are perpendicular to x or y axis
        yDelta_a = P2.Y - P1.Y
        xDelta_a = P2.X - P1.X
        yDelta_b = P3.Y - P2.Y
        xDelta_b = P3.X - P2.X

        # checking whether the Line of the two points are vertical
        if math.fabs(xDelta_a) <= 0.000000001 and math.fabs(yDelta_b) <= 0.000000001:
            # The points are pependicular and parallel to X-Y axis
            return False
        if math.fabs(yDelta_a) <= 0.0000001:
            # Line of two point are perpendicular to x-axis 1
            return True
        elif math.fabs(yDelta_b) <= 0.0000001:
            # Line of two point are perpendicular to x-axis 2
            return True
        elif math.fabs(xDelta_a)<= 0.000000001:
            # Line of two point are perpendicular to y-axis 1
            return True
        elif math.fabs(xDelta_b)<= 0.000000001:
            # Line of two point are perpendicular to y-axis 2
            return True
        else:
            return False
    # Private Function
    def __CalcCircle(self,P1,P2,P3): # Calculate the radius and the center of Giving Circle
        yDelta_a = P2.Y - P1.Y
        xDelta_a = P2.X - P1.X
        yDelta_b = P3.Y - P2.Y
        xDelta_b = P3.X - P2.X

        if math.fabs(xDelta_a) <= 0.000000001 and math.fabs(yDelta_b) <= 0.000000001:
            self.Center.X= 0.5 * (self.P2.X + self.P3.X)
            self.Center.Y= 0.5 * (self.P1.Y + self.P2.Y) # Calculate the Center of giving circle
            self.Radius= calculateDistance(self.Center, self.P1) ## Calculate the Radius of giving circle

        # IsPerpendicular() assure that xDelta(s) are not zero
        aSlope = yDelta_a / xDelta_a
        bSlope = yDelta_b / xDelta_b

        if math.fabs(aSlope - bSlope) <= 0.000000001:
            # checking whether the given points are colinear.
            self.Center=P(-1,-1)
            self.Radius=-1

        # Calculate the Center
        self.Center.X = (aSlope * bSlope * (P1.Y - P3.Y) + bSlope * (P1.X + P2.X)
                              - aSlope * (P2.X+P3.X)) / (2 * (bSlope - aSlope))
        self.Center.Y = -1 * (self.Center.X - (P1.X + P2.X )/ 2) / aSlope + (P1.Y + P2.Y) / 2

        #Calculate the Radius
        self.Radius = calculateDistance(self.Center, P1)

    def getRadius(self):  #Getting The Radius of Cicle
        return self.Radius
    def getCenter(self):  #Getting The Center Of Circle
        return self.Center




def calculateDistance(P1, P2):  # Find the distance between two points by using Euclidean
    dist = math.sqrt((P2.X - P1.X) ** 2 + (P2.Y - P1.Y) ** 2)
    return dist


def DoLinesIntersect(L1,L2):
    # Denominator
    d=(L2.p2.Y - L2.p1.Y) * (L1.p2.X - L1.p1.X) - (L2.p2.X - L2.p1.X) * (L1.p2.Y - L1.p1.Y)
    # n_a and n_b are calculated as seperate values for readability
    n_a = (L2.p2.X - L2.p1.X) * (L1.p1.Y - L2.p1.Y) - (L2.p2.Y - L2.p1.Y) * (L1.p1.X - L2.p1.X)
    n_b = (L1.p2.X - L1.p1.X) * (L1.p1.Y - L2.p1.Y) - (L1.p2.Y - L1.p1.Y) * (L1.p1.X - L2.p1.X)

    if d == 0:
        if n_a == 0 and n_b == 0:
            return "coincidente"
        else:
            return "perallal"
    else:
        Ua=n_a/d
        Ub=n_b/d

    return P(L1.p1.X + (Ua * (L1.p2.X - L1.p1.X)),L1.p1.Y + (Ua * (L1.p2.Y - L1.p1.Y)))

def main():
    p1 = P(6, 3)
    p2 = P(4, 1)
    p3 = P(2.59, 1.59)

    circle= Circle(p1,p2,p3)

    Radius =circle.getRadius()
    centerOfCircle = circle.getCenter()

    print("Radius of Circle :{}".format(Radius))
    print("The Center of Circle ",end="")
    centerOfCircle.print()


if __name__ == '__main__':
    main()
