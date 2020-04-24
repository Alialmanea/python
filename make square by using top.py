import math


class coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print(self):
        print("X={}  Y={}".format(self.x,self.y))


class square:
    def __init__(self,coordinate_1,coordinate_2):
        self.coordinate_1=coordinate_1;
        self.coordinate_2=coordinate_2;
    def area(self):
        a=oklid(self.coordinate_2.x,self.coordinate_2.x,self.coordinate_2.y,self.coordinate_1.y)
        return (a**2)/2 # area= 1/2 * a**2
    def perimeter(self):
        return 4*math.sqrt(self.area()) # perimeter= 4*area**0.5



def oklid(x1,x2,y1,y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

def main():
    coordinate_1=coordinate(1,2)
    coordinate_2=coordinate(3,4)



    kare=square(coordinate_1,coordinate_2)
    kare.coordinate_1.print()
    kare.coordinate_2.print()

    print("(1,2) (3,4) öklidi : {}".format(oklid(coordinate_2.x,coordinate_1.x,coordinate_2.y,coordinate_1.y)))
    print("karenın alanı :{}".format(kare.area()))
    print("karenın çevresi :{}".format(kare.perimeter()))


if __name__ == '__main__':
    main()
