class Rectangle:
    def __init__(self, length, width):
        self.__length = length  # Private attribute
        self.__width = width    # Private attribute

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))
rect1 = Rectangle(length1, width1)
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))
rect2 = Rectangle(length2, width2)
if rect1 < rect2:
    print("The first rectangle has a smaller area than the second rectangle.")
elif rect2 < rect1:
    print("The second rectangle has a smaller area than the first rectangle.")
else:
    print("Both rectangles have the same area.")

