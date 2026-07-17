class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
    
    def accept(self):
        radius = float(input("Enter value of radius: "))
        self.radius = radius
    
    def calculateArea(self):
        area = Circle.PI * self.radius * self.radius
        self.area = area

    def calculateCircumference(self):
        circumference = 2 * Circle.PI * self.radius
        self.circumference = circumference

    def display(self):
        print("Radius of circle is: ", self.radius)
        print(f"Area of circle is: {self.area:.4f}")
        print(f"Circumference of circle is: {self.circumference:.4f}")

cObj = Circle()

cObj.accept()
cObj.calculateArea()
cObj.calculateCircumference()
cObj.display()

cObj1 = Circle()

cObj1.accept()
cObj1.calculateArea()
cObj1.calculateCircumference()
cObj1.display()

