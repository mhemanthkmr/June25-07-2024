class calculator :

    def __init__(self,a,b):
        self.a =a
        self.b =b
        pass

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
calc = calculator(10,20)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())