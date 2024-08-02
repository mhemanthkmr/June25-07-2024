class person :
    def __init__(self,name, id) :
        self.name  = name 
        self.id = id

    def display(self):
        print(f"Name : {self.name} & ID : {self.id}")

class employee (person):
    def employee(self):
        print("employee class")
    pass

class citizen (employee):
    def citizen (self):
        print(" citizen class")
    pass

obj1 = person ("ajees",20)
obj1.display ()

obj1 = employee ("ajees",20)
obj1.employee ()

obj1 = citizen  ("ajees",20)
obj1.citizen ()
