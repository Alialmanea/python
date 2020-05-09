class P:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y

class Line:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

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
    p1 = P(0, 1)
    p2 = P(4, 3)
    p3 = P(0, 3)
    p4 = P(3, 0)

    line_a = Line(p1, p2)
    line_b = Line(p3, p4)

    if type(DoLinesIntersect(line_a,line_b)) == str:
        print("İs Not intersect : it is {}! ".format(DoLinesIntersect(line_a,line_b)))
    else:
        print("The Intersect point of lines is: ({}, {})".format(DoLinesIntersect(line_a,line_b).X
              ,DoLinesIntersect(line_a,line_b).Y))



if __name__ == '__main__':
    main()
