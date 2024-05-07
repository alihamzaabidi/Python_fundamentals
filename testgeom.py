class Rectangle:
    def __init__(self,tl,br):
        self.tl=tl
        self.br=br
        self.width=abs(tl.x-br.x)
        self.height=abs(tl.y-br.y)
    def area(self): 
        return self.width*self.height 

class Coordinate: 
     def __init__(self,x,y):
        self.x=x
        self.y=y
     def distance(self,another): 
        import math
        xdist=abs(self.x-another.x)
        ydist=abs(self.y-another.y)
        return math.sqrt(xdist**2+ydist**2)


def test_rectangle():
    point1x_in = int(input("Enter the x axis of point one ="))
    point1y_in = int(input("Enter the y-axis of point one ="))
    obj_1 = Coordinate(point1x_in, point1y_in)
    print(" ")
    point2x_in = int(input("Enter the x axis of point second ="))
    point2y_in = int(input("Enter the y-axis of point second ="))
    
    obj_2 = Coordinate(point2x_in, point2y_in)
    output_rectangular = Rectangle(obj_1, obj_2)
    print(" ")
    print("The area of rectangle between two coordinate one point {},{} and the another point {},{} is = ".format(point1x_in,point1y_in,point2x_in,point2y_in),output_rectangular.area())
    print(" ")
    print("***Calculate distance between two point***")
    print(" ")
    point3x_in = int(input("Enter the x axis of point Third ="))
    point3y_in = int(input("Enter the y-axis of point third ="))
    obj_3 = Coordinate(point3x_in, point3y_in)
#    distance_between = Coordinate(obj_1, obj_3)
    
    print("The distance between one point {},{} and the another point {},{} is = ".format(point1x_in,point1y_in,point3x_in,point3y_in),obj_1.distance(obj_3))
    
def main():
    test_rectangle()

main()


