import importlib 
from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter


# Dynamically import the necessary modules
cuboid_module = importlib.import_module("graphics.3D-graphics.cuboid")
sphere_module = importlib.import_module("graphics.3D-graphics.sphere")

# Function aliases
cuboid_area = cuboid_module.surface_area
cuboid_volume = cuboid_module.volume
sphere_area = sphere_module.surface_area
sphere_volume = sphere_module.volume

def main():
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Cuboid")
    print("4. Sphere")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        print("Rectangle Area:", rect_area(length, breadth))
        print("Rectangle Perimeter:", rect_perimeter(length, breadth))
    
    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        print("Circle Area:", circle_area(radius))
        print("Circle Perimeter:", circle_perimeter(radius))
    
    elif choice == 3:
        length = float(input("Enter the length of the cuboid: "))
        width = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        print("Cuboid Surface Area:", cuboid_area(length, width, height))
        print("Cuboid Volume:", cuboid_volume(length, width, height))
    
    elif choice == 4:
        radius = float(input("Enter the radius of the sphere: "))
        print("Sphere Surface Area:", sphere_area(radius))
        print("Sphere Volume:", sphere_volume(radius))
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
