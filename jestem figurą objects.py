
class Shape():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Rectangle(Shape):
    def __init__(self, a, b):
        Shape.__init__(self, a, a)
        self.a = a
        self.b = b
        
    def calculate_perimeter(self):
        s = 2 * (self.a + self.b)
        return s

    def what_am_i(self):
        print("Jestem figurą: prostokątem")
    
class Square(Shape):
    def __init__(self, a):
        Shape.__init__(self, a, a)
        self.a = a

    def calculate_perimeter(self):
        s = 4 * (self.a)
        return s

    def what_am_i(self):
        print("Jestem figurą. kwadratem")
