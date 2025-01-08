class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Input for the first rectangle
length1 = float(input("Enter the length of the first rectangle: "))
breadth1 = float(input("Enter the breadth of the first rectangle: "))
rect1 = Rectangle(length1, breadth1)

# Input for the second rectangle
length2 = float(input("Enter the length of the second rectangle: "))
breadth2 = float(input("Enter the breadth of the second rectangle: "))
rect2 = Rectangle(length2, breadth2)

# Displaying areas and perimeters
print(f"Area of first rectangle: {rect1.area()}")
print(f"Perimeter of first rectangle: {rect1.perimeter()}")
print(f"Area of second rectangle: {rect2.area()}")
print(f"Perimeter of second rectangle: {rect2.perimeter()}")

# Comparing the areas
if rect1.area() > rect2.area():
    print("The first rectangle has a larger area.")
elif rect1.area() < rect2.area():
    print("The second rectangle has a larger area.")
else:
    print("Both rectangles have the same area.")

