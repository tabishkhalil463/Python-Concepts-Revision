class Animal:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some animal sound"
    
    def move(self):
        return f"{self.name} moves around"
    
    def describe(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    
    def __init__(self, name, breed):
        # Call parent's __init__ method
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof! Woof!"
    
    def move(self):
        return f"{self.name} runs and wags tail"
    
    def describe(self):
        return f"{self.name} is a {self.breed} dog"

class Cat(Animal):
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow!"
    
    def move(self):
        return f"{self.name} walks gracefully"
    
    def describe(self):
        return f"{self.name} is a {self.color} cat"


print("=== ANIMAL EXAMPLE ===")
generic_animal = Animal("Unknown", "Unknown")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(f"Generic Animal: {generic_animal.make_sound()}")
print(f"Dog: {dog.make_sound()}")
print(f"Cat: {cat.make_sound()}")
print()

print(f"Generic Animal: {generic_animal.move()}")
print(f"Dog: {dog.move()}")
print(f"Cat: {cat.move()}")
print()

print(f"Generic Animal: {generic_animal.describe()}")
print(f"Dog: {dog.describe()}")
print(f"Cat: {cat.describe()}")
print()


import math

class Shape:
    
    def __init__(self, name):
        self.name = name
    
    def calculate_area(self):
        return 0
    
    def calculate_perimeter(self):
        return 0
    
    def describe(self):
        return f"A {self.name}"

class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def describe(self):
        return f"A circle with radius {self.radius}"

class Rectangle(Shape):    
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    def describe(self):
        return f"A rectangle with length {self.length} and width {self.width}"

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def describe(self):
        return f"A triangle with sides {self.side1}, {self.side2}, {self.side3}"

print("=== SHAPE CALCULATIONS ===")

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape.describe()}")
    print(f"Area: {shape.calculate_area():.2f}")
    print(f"Perimeter: {shape.calculate_perimeter():.2f}")
    print()






