# module name rectangle.py

class Rectangle: # Rectangle class
    # init method accepts width and height of Rectangle
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    #perimeter method retuns the perimeter of the rectangle
    def perimeter(self):
        return 2*(self.__width + self.__height)

    #perimeter method retuns the area of the rectangle
    def area(self):
        return self.__width * self.__height


def test_Rectangle():
    print("Testing Rectangle ....!!!")
    obj = Rectangle(7, 8)
    out_rec = obj.perimeter()
    print("The width of rectangular is {} and height of rectangular is {} ".format(7,8))
    print("The perimeter of the rectangular is = ",out_rec)


def test_area():
    print("Testing Area....!!!")
    obj = Rectangle(4,9)
    out_area = obj.perimeter()
    print("The width of rectangular is {} and height of rectangular is {} ".format(4,9))
    print("The perimeter of the rectangular is = ",out_area)

def main():
    test_Rectangle()
    print(" ")
    test_area()

main()
