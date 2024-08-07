class person:
    def __init__(self, name, id):
        self.name= name
        self.id= id
        
    def display(self):
        print(f'Name={self.name} & Id={self.id}')
        
class emp(person):
    def emp(self):
        print(f'Name={self.name} & Id={self.id}')
        print("employee class")
        
obj1=emp("dhanu",20242001)
obj1.emp()
