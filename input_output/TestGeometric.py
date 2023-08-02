from Circle import Circle
from Retangle import Rectangle


def main():
    circle = Circle(5)
    # circle.setColor("Green")
    # print(circle)
    # print("The circle radius :", circle.getRadius())
    # print("The circle area :", circle.getArea())
    # print(circle.printCircle())

    rectangle = Rectangle(5, 10)
    # print("The rectangle perimeter :", rectangle.getPerimeter())
    # print("The rectangle area :", rectangle.getArea())
    displayObject(circle)
    displayObject(rectangle)


def displayObject(g):
    print("Area is ", g.getArea())
    print("Perimeter is ", g.getPerimeter())
    if isinstance(g, Circle):
        print(g.getDiameter())
    elif isinstance(g, Rectangle):
        print("Width of Rectangle is ", g.getWidth())
        print("Height of Rectangle is ", g.getHeight())


main()
