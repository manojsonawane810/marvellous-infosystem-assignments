class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def accept(self):
        value1 = float(input("Enter first number: "))
        value2 = float(input("Enter second number: "))
        self.value1 = value1
        self.value2 = value2

    def addition(self):
        return self.value1 + self.value2
    
    def substraction(self):
        return self.value1 - self.value2
    
    def multiplication(self):
        return self.value1 * self.value2
    
    def division(self):
        division = None
        try:
            division = self.value1 / self.value2
            print("Division is sucessful")
        except ZeroDivisionError as zObj:
            print("Exception occured due to 0 operand value of 2nd number: ", zObj)
        
        return division
    
aObj = Arithmetic()

aObj.accept()
add = aObj.addition()
sub = aObj.substraction()
multi = aObj.multiplication()
divi = aObj.division()

print(f"Addition of {aObj.value1} and {aObj.value2} is {add}")
print(f"Substraction of {aObj.value1} and {aObj.value2} is {sub:.4f}")
print(f"Multiplication of {aObj.value1} and {aObj.value2} is {multi:.4f}")
if divi != None:
    print(f"Division of {aObj.value1} and {aObj.value2} is {divi:.4f}")

aObj1 = Arithmetic()

aObj1.accept()
add = aObj1.addition()
sub = aObj1.substraction()
multi = aObj1.multiplication()
divi = aObj1.division()

print(f"Addition of {aObj1.value1} and {aObj1.value2} is {add}")
print(f"Substraction of {aObj1.value1} and {aObj1.value2} is {sub:.4f}")
print(f"Multiplication of {aObj1.value1} and {aObj1.value2} is {multi:.4f}")

if divi != None:
    print(f"Division of {aObj1.value1} and {aObj1.value2} is {divi:.4f}")