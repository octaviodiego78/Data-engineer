class Shape:

    def __init__(self):
        self.name = 'Shape'


    def get_area(self) -> float:
        ...
    
class Rectangle(Shape):
    
    def __init__(self, base:float, height:float):
        super().__init__() #Calls the parent
        self.base = base
        self.height = height
        self.name = "Rectangle"

    def get_area(self) -> float:
        return self.base * self.height


class Square(Rectangle):
    def __init__(self, side:float):
        super().__init__(side,side) #Calls the parent class which is Rectangle and fills REctangle parameters with this arguments
        self.name = 'Square'

square = Rectangle(base=5,height=5)
print(square.get_area())
