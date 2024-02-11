class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area() and self.perimeter()
        return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area() and self.perimeter()
        return NotImplemented


if __name__ == '__main__':
    rect1 = Rectangle(5, 4)
    rect2 = Rectangle(3, 6)
    rect3 = Rectangle(5, 4)
    rect4 = Rectangle(8, 2)


print("Rect1 == Rect2:", rect1 == rect2)
print("Rect1 == Rect3:", rect1 == rect3)
print("Rect2 < Rect3:", rect2 < rect3)
print("Rect1 < Rect4:", rect1 < rect4)