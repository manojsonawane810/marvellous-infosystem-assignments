class Demo:
    value = None
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2
    
    def fun(self):
        print("Inside fun method")
        print("Instance variable no1 value is: ", self.no1)
        print("Instance variable no2 value is: ", self.no2)
    
    def gun(self):
        print("Inside gun method")
        print("Instance variable no1 value is: ", self.no1)
        print("Instance variable no2 value is: ", self.no2)
    
obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()
